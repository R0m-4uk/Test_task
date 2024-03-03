from core.models import RoleOfGroup


def get_user_role():
    user_role_qs = RoleOfGroup.objects.filter(pk=2)
    if len(user_role_qs) == 0:
        return None
    return user_role_qs[0]