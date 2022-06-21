from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone
from rest_framework import status
from rest_framework.exceptions import APIException

class RegistedMoreThanTreeDaysUser(BasePermission):
    """
    가입일 기준 3일 이상 지난 사용자만 접근 가능
    """
    message = '가입 후 3일 이상 지난 사용자만 사용하실 수 있습니다.'
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.join_date < (timezone.now() - timedelta(minutes=3)))


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(datail=detail, code=code)


class IsAdminOrAuthenticateReadOnly(BasePermission):
    # admin 사용자는 모두 가능, 로그인 사용자는 조회만 가능
    SAFE_METHODS = ('GET', )
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response = {
                "detail": "login plz",
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        # 로그인 사용자가 get 요청 = True
        if user.is_authenticated and request.method in self.SAFE_METHODS:
            return True

        # admin or 가입일이 일정 기간을 넘은 유저 = True
        if user.is_authenticated and user.is_admin or user.join_date < (timezone.now() - timedelta(minutes=3)):
            return True

        return False