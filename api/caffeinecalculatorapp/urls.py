from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

# NOTE: binding http methods to the required/corresponding action for each view
# caffeineitem_list = views.CaffeineItemViewSet.as_view({"get": "list", "post": "create"})
# caffeineitem_detail = views.CaffeineItemViewSet.as_view(
#     {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
# )
# consumeditem_list = views.ConsumedItemViewSet.as_view({"get": "list", "post": "create"})
# consumeditem_detail = views.ConsumedItemViewSet.as_view(
#     {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
# )
# consumeditem_increase_first_caffeine_item_by_one = views.ConsumedItemViewSet.as_view(
#     {"post": "increase_first_caffeine_item_by_one"}
# )
# user_list = views.UserViewSet.as_view({"get": "list"})
# user_detail = views.UserViewSet.as_view({"get": "retrieve"})

# NOTE: router for ViewSets
router = DefaultRouter()
router.register(r"caffeine-items", views.CaffeineItemViewSet, basename="caffeineitem")
router.register(r"consumed-items", views.ConsumedItemViewSet, basename="consumeditem")
router.register(r"users", views.UserViewSet, basename="user")

urlpatterns = [
    # NOTE: urls for api root
    path("", views.api_root),
    # NOTE: urls for function-based views
    # path("caffeine-items/", views.caffeine_item_list, name="caffeine-items-list"),
    # path(
    #     "caffeine-items/<int:pk>/",
    #     views.caffeine_item_detail,
    #     name="caffeine-items-detail",
    # ),
    # NOTE: urls for class-based views
    # path("caffeine-items/", views.CaffeineItemList.as_view(), name="caffeineitem-list"),
    # path(
    #     "caffeine-items/<int:pk>/",
    #     views.CaffeineItemDetail.as_view(),
    #     name="caffeineitem-detail",
    # ),
    # path("consumed-items/", views.ConsumedItemList.as_view(), name="consumeditem-list"),
    # path(
    #     "consumed-items/<int:pk>/",
    #     views.ConsumedItemDetail.as_view(),
    #     name="consumeditem-detail",
    # ),
    # path("users/", views.UserList.as_view(), name="user-list"),
    # path(
    #     "users/<int:pk>/",
    #     views.UserDetail.as_view(),
    #     name="user-detail",
    # ),
    # NOTE: urls for ViewSets
    # path("caffeine-items/", caffeineitem_list, name="caffeineitem-list"),
    # path("caffeine-items/<int:pk>/", caffeineitem_detail, name="caffeineitem-detail"),
    # path("consumed-items/", consumeditem_list, name="consumeditem-list"),
    # path("consumed-items/<int:pk>/", consumeditem_detail, name="consumeditem-detail"),
    # path(
    #     "consumed-items/<int:pk>/increase-first-caffeine-item-by-one/",
    #     consumeditem_increase_first_caffeine_item_by_one,
    #     name="consumeditem-increase-first-caffeine-item-by-one",
    # ),
    # path("users/", user_list, name="user-list"),
    # path("users/<int:pk>/", user_detail, name="user-detail"),
    # NOTE: urls for ViewSets with router
    path("", include(router.urls)),
]
