from core.models import Group, Product


def get_new_name_group(group: Group):
    return f"{group.product_id.name} {group.pk}"


# Если продукт создался, то должна создастся сразу же группа

# Если продукт не запущен:
#   1. Добавляем людей в группу пока он не запущен

# 1. amount_students в двое больше чем min_group_size, при этом если group
# 2. amount_students в двое больше чем min_group_size
def need_create_group(product: Product, group: Group):
    return f"{group.product_id.name} {group.pk}"
