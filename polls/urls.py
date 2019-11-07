from django.urls import path
from .views import polls_detail, polls_list
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls


router = DefaultRouter()
schema_view = get_swagger_view(title='Polls API')
router.register('polls', PollViewSet, base_name='polls')


urlpatterns = [
	# path("polls/", polls_list, name="polls_list"),
	# path("polls/<int:pk>/", polls_detail, name="polls_detail"),
	path("polls/", PollList.as_view(), name="polls_list"),
	path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
	# path("choices/", ChoiceList.as_view(), name="choice_list"),
	path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
	# path("vote/", CreateVote.as_view(), name="create_vote"),
	path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
	path("users/", UserCreate.as_view(), name="user_create"),
	path("login/", LoginView.as_view(), name="login"),
	# path(r'swagger-docs/', schema_view),
	path(r'docs/', include_docs_urls(title='Polls API')),
]
