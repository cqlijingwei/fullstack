from models.user import (get_user_total, get_user_info, update_user_info, del_user, add_user)


def search_info(kwargs: dict):
    """
    current_page
    page_size
    """
    current_page = int(kwargs.get("current_page", 1))
    page_size = int(kwargs.get("page_size", 5))

    total = get_user_total()
    user_info = get_user_info(current_page, page_size)

    return {"employees": user_info, "total": total}


def user_edit(kwargs: dict):
    if not kwargs.get("userid"):
        return 0
    salary = int(kwargs.get("salary", -1))
    if salary < 0:
        return 0
    if not update_user_info(kwargs):
        return 0
    return 1


def user_del(kwargs: dict):
    userid = int(kwargs.pop("userid", 0))
    if not userid:
        return 0
    return del_user(userid=userid)


def user_add(kwargs):
    first_name, last_name, salary = kwargs.get("firstName"), kwargs.get("lastName"), kwargs.get("salary")
    if not any([first_name, last_name, salary]):
        return 0
    if int(salary) < 0:
        return 0
    return add_user(params=[first_name, last_name, salary])
