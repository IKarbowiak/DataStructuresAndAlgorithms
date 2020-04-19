class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True

    groups = group.get_groups()
    for group in groups:
        res = is_user_in_group(user, group)
        if res:
            return True

    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child_user = "child_user"
child.add_user(child_user)

child.add_group(sub_child)
parent.add_group(child)


print(is_user_in_group(sub_child_user, parent))
# should return True - sub_child_user is in parent group

print(is_user_in_group(sub_child_user, child))
# should return True - sub_child_user is in child group

print(is_user_in_group(sub_child_user, sub_child))
# should return True - sub_child_user is in sub_child group

print(is_user_in_group(child_user, sub_child))
# should return False - child_user is in not sub_child group

print(is_user_in_group(child_user, child))
# should return True - child_user is in child group

print(is_user_in_group(child_user, parent))
# should return True - child_user is in parent group
