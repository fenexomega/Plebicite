from .forms import LoginForm

def include_login_form(request):
	loginform = LoginForm()
	return {'loginform':loginform}