from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from iq_app.models import User, Solution, Registration
from iq_app.forms import UserForm, RegistrationForm


from django.shortcuts import render_to_response

from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

# Create your views here.

def index(request):
    context = {}
    context['name'] = 'my name'
    # print request.user.username
    return render(request, "iq_app/index.html", context)


def signup(request):
    context = {}
    context['action'] = '/uche/account/iq'
    context['title'] = 'iq_app - iq'
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        registration_form = RegistrationForm(request.POST)

        if user_form.is_valid() and registration_form.is_valid():
            user = user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            registration = registration_form.save(commit=False)
            registration.user = user
            registration.age = request.POST['age']
            registration.save()
            # print form
            return HttpResponseRedirect('/iq_app')

    else:
        context['form'] = UserForm()
        context['registerform'] = RegistrationForm()

    return render(request, 'iq_app/signup.html', context)



def user_login(request):
	# If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
        # because the request.POST.get('<variable>') returns None, if the value does not exist,
        # while the request.POST['<variable>'] will raise key error exception
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/iq_app/home')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your iq account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            # print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'iq_app/login.html', {})



# Use the login_required() decorator to ensure only those logged in can access the view.
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/iq_app/')



def home(request):

	return render(request, 'iq_app/home.html', {})


def iq_test(request):

    # posting all question from django admin to template
    context = {}
    context['question'] = Solution.objects.all()
    # End of the posting all question from django admin to template
    #
    # Placing all answers from django admin to an empty list
    answer = []
    for i in context['question']:
        answer.append(str(i.answer))
    # End of Placing all answers from django admin to an empty list
    # 
    # Placing all uuid or id from django admin to an empty list
    uuid = []
    for i in context['question']:
        uuid.append(str(i.uuid))
    # End of Placing all uuid or id from django admin to an empty list
    
    request.session['answer'] = answer
    request.session['uuid'] = uuid

    # request.session['answer'] = answer
    # print answer
    # print uuid
    # print request.POST
    return render(request, 'iq_app/iq_test.html', context)


def result_check(request):
    context = {}
    answer = request.session['answer']
    uuid = request.session['uuid']

    # getting all user checked answers and matching it with admin answer
    if request.method == 'POST':
        user_checks = []
        for i in uuid:
            a = request.POST.get(str(i))
            user_checks.append(a)
        # print user_checks

        b = 0
        score = 0
        while b <= len(answer) - 1:
            if answer[b] == user_checks[b]:
                print 'correct', answer[b], user_checks[b]
                score += 2
            else:
                print 'wrong', answer[b], user_checks[b]
                
            b += 1
        print 'score', score
        # end of getting all user checked answers and matching it with admin answer
    
        
        # How to get user name and age from django admin
        user_obj = []
        user_obj = User.objects.get(username = request.user)
        print 'name', user_obj

        user_age = []
        user_age = Registration.objects.get(user = user_obj)
        print 'age', user_age.age
        # end of getting all user checked answers and matching it with admin answer

        # calculation to get the iq score
        iq = (float(score) / float(user_age.age)) * 100

        print 'Your IQ is ', int(iq)
        # end of calculation to get the iq score

        # to get percentile and range of iq
        if iq < 70:
            # print "2.2%  of people are in these range, which is Extremely Low, "
            iq_range = "2.2%  of people are in these range, which is Extremely Low, "
        elif iq <= 79:
            # print "6.7%  of people are in these range, which is a Borderline, "
            iq_range = "6.7%  of people are in these range, which is a Borderline, "
        elif iq <= 89:
            # print "16.1%  of people are in these range, which is a Low Average, "
            iq_range = "16.1%  of people are in these range, which is a Low Average, "
        elif iq <= 109:
            # print "50%  of people are in these range, which is Average, "
            iq_range = "50%  of people are in these range, which is Average, "
        elif iq <= 119:
            # print "16.1%  of people are in these range, which is High Average, "
            iq_range = "16.1%  of people are in these range, which is High Average, "
        elif iq <= 129:
            # print "6.7%  of people are in these range, which is Superior, "
            iq_range = "6.7%  of people are in these range, which is Superior, "
        else:
            # print "2.2%  of people are in these range, which is Very Superior, "
            iq_range = "2.2%  of people are in these range, which is Very Superior, "
        # to get percentile and range of iq

        
        context['iq'] = int(iq)
        context['iq_range'] = iq_range

    return render(request, 'iq_app/result.html', context)


# def result(request):

#     return render(request, 'iq_app/result.html', context)
