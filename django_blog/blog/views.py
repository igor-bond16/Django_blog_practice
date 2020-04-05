from django.shortcuts import render,redirect
from .models import Friend,Message
from .forms import FindForm,CheckForm,FriendForm,MessageForm
from django.db.models import Count,Sum,Avg,Min,Max
from django.core.paginator import Paginator

#from django.db.models import Q

# Create your views here.
def home(request,num=1):
    data = Friend.objects.all()
    pagenator = Paginator(data,3)
    page_object = pagenator.page(num)
    #page_number = request.GET.get('page')
    params = {
            'title':'Hello',
            'message':'',
            'data':page_object,
            }
    return render(request,'blog/blog_home.html',params)

def create(request):
    if(request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect('Http://localhost:8000/blog/home/')
    params = {
            'title':'Hello',
            'form':FriendForm()
            }
    return render(request,'blog/create.html',params)

def edit(request,num):
    obj = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend = FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect('http://localhost:8000/blog/home/')
    params = {
            'title':'Hello',
            'id':num,
            'form':FriendForm(instance=obj),
            }
    return render(request,'blog/edit.html',params)

def delete(request,num):
    friend = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend.delete()
        return redirect('http://localhost:8000/blog/home/')
    params = {
            'title':'Hello',
            'id':num,
            'obj':friend,
            }
    return render(request,'blog/delete.html',params)

def find(request):
    if(request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        str = request.POST['find']
        list = str.split()
        data = Friend.objects.all()[int(list[0]):int(list[1])]
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
            'title':'Hello',
            'message':msg,
            'form':form,
            'data':data,
            }
    return render(request,'blog/find.html',params)

def check(request):
    params = {
            'title':'Hello',
            'message':'check validation.',
            'form':FriendForm(),
            }
    if (request.method == 'POST'):
        obj = Friend()
        form = FriendForm(request.POST,instance=obj)
        params['form'] = form
        if (form.is_valid()):
            params['message'] = 'OK'
        else:
            params['message'] = 'no good.'
    return render(request,'blog/check.html',params)

def message(request,page=1):
    if(request.method == 'POST'):
        obj = Message()
        form = MessageForm(request.POST,instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data,5)
    page_obj = paginator.page(page)
    params = {
        'title':'Message',
        'form':MessageForm(),
        'data':page_obj,
            }
    return render(request,'blog/message.html',params)








