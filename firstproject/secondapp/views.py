from django.shortcuts import render

def count(request):
    nickname=request.GET['nickname']
    return render(request, "count.html",{'nickname':nickname})

def countResult(request):
    w_input=request.GET['w_input']

    wordsplit=w_input.split()
    countDict={}

    for w in wordsplit:
        if w in countDict:
            countDict[w]+=1
        else:
            countDict[w]=1
    return render(request,'countResult.html', {'w_input':w_input, 'len':len(wordsplit), 'countDict':countDict.items()})
