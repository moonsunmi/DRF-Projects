from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSimpleSerializer, TodoDetailSerializer, TodoCreateSerializer


class TodosAPIView(APIView):
    """투두 전체 조회용 APIView 클래스.
    제목(title), 완료 여부(is_complete), 중요 여부(is_important)를 담는다."""

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        """투두 전체를 조회한다."""
        todos = Todo.objects.filter(is_complete=False)
        serializer = TodoSimpleSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        """투두 한 개를 등록한다."""
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoAPIView(APIView):
    """투두 하나의 전체 정보 조회용 APIView 클래스."""

    # noinspection PyMethodMayBeStatic
    def get(self, request, pk):
        """투두 하나를 조회한다."""
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # noinspection PyMethodMayBeStatic
    def put(self, request, pk):
        """투두 하나를 수정한다.
        논리 에러가 있는 듯한데..?
        투두를 하나 만들 때는, is_complete 필드가 필요 없지만
        투두를 수정할 때는, is_complete 필드를 수정할 때도 있다.
        따라서 새 serializer를 만들어야 할 것 같다.
        """

        todo = get_object_or_404(Todo, id=pk)  # django에서는 pk= ... 이렇게 적었는데..
        serializer = TodoCreateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DonesTodoAPIView(APIView):
    """완료된 투두들을 다루는 APIView 클래스."""

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        dones = Todo.objects.filter(is_complete=True)  # complete와 done 표현을 맞춰 주는 게 좋은가?
        serializer = TodoSimpleSerializer(dones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DoneTodoAPIView(APIView):
    """투두 하나를 완료 상태로 바꾸는 APIView 클래스."""

    # noinspection PyMethodMayBeStatic
    def get(self, request, pk):  # 간단한 요청이라 get 메서드를 이용했다고 한다.
        done = get_object_or_404(Todo, id=pk)
        done.complete = True
        done.save()
        serializer = TodoDetailSerializer(done)
        return Response(serializer.data, status=status.HTTP_200_OK)
