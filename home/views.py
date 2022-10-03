from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.

def index(request):

    return redirect("/dashboard")

def dashboard(request):

    
    from home.models import Data

    data = Data.objects.all()
    
    intensitydict = dict()

    for i in data:

        try:
            if i.region not in intensitydict:
                if i.region != "":
                    intensitydict[i.region] = int(i.intensity)
            else:
                intensitydict[i.region] += int(i.intensity)
        except Exception as e:
            print(e)

    likelihooddict = {}

    for i in data:
        
        if i.likelihood not in likelihooddict:
            if i.likelihood != "":
                likelihooddict[i.likelihood] = 1
        else:
            likelihooddict[i.likelihood] +=1
    
    relevancedict = {}

    for i in data:
        
        if i.relevance not in relevancedict:
            if i.relevance != "":
                relevancedict[i.relevance] = 1
        else:
            relevancedict[i.relevance] +=1


    topicdict = {}
    for i in data:
        if i.topic not in topicdict:
            if i.topic != "":
                topicdict[i.topic] = 1
        else:
            topicdict[i.topic] +=1



    topfivetopics = sorted(topicdict, key=topicdict.get, reverse = True)[:5]
    toptopicdict = {}

    for i in topfivetopics:
        toptopicdict[i] = topicdict[i]
    
    countrydict = {}

    for i in data:
        
        if i.country not in countrydict:
            if i.country != "":
                countrydict[i.country] = 1
        else:
            countrydict[i.country] +=1
        
    print(len(countrydict))

    topcountrylist = sorted(countrydict ,key=countrydict.get , reverse=True)[:10]
    topcountrydict = {}

    for i in topcountrylist:
        topcountrydict[i] = countrydict[i]


    end_year_filter = set([i.end_year for i in data if i.end_year !=""])
    topic_filter = set([i.topic for i in data if i.topic !=""] )
    region_filter = set([i.region for i in data if i.region !=""] )
    source_filter = set([i.source for i in data if i.source !=""] )
    sector_filter = set([i.sector for i in data if i.sector !=""] )
    country_filter = set([i.country for i in data if i.country !=""] )

    parms ={
        "data":data,
        "intensitydict":intensitydict,
        "likelihooddict":likelihooddict,
        "relevancedict":relevancedict,
        "topic":toptopicdict,
        "country" :topcountrydict,

        "end_year_filter":end_year_filter,
        "topic_filter": topic_filter,
        "region_filter": region_filter,
        "source_filter": source_filter,
        "sector_filter": sector_filter,
        "country_filter": country_filter,
    }

    return render(request, "home/dashboard.html",parms )




def addData(request):
    import json
    from home.models import Data
    # jsondatafile  = open("datafiles/jsondata.json", "r")
    # jsondata = jsondatafile.read()
    # dictdata = json.loads(jsondata)


    # for i in dictdata:
    #     print(i)

    #     Data.objects.create(**i)



def datafilter(request, fstr):
    from home.models import Data

    field = fstr.split("-")[0]
    value = fstr.split("-")[1]

    data = Data.objects.all()

    end_year_filter = set([i.end_year for i in data if i.end_year !=""])
    topic_filter = set([i.topic for i in data if i.topic !=""] )
    region_filter = set([i.region for i in data if i.region !=""] )
    source_filter = set([i.source for i in data if i.source !=""] )
    sector_filter = set([i.sector for i in data if i.sector !=""] )
    country_filter = set([i.country for i in data if i.country !=""] )

    if field == "end_year":
        data = Data.objects.filter(end_year=value)
    elif field == "topic":
        data = Data.objects.filter(topic=value)
    elif field == "region":
        data = Data.objects.filter(region=value)
    elif field == "source":
        data = Data.objects.filter(source=value)
    elif field == "sector":
        data = Data.objects.filter(sector=value)
    elif field == "country":
        data = Data.objects.filter(country=value)
    else:
        data = Data.objects.all()

    intensitydict = dict()

    for i in data:

        try:
            if i.region not in intensitydict:
                if i.region != "":
                    intensitydict[i.region] = int(i.intensity)
            else:
                intensitydict[i.region] += int(i.intensity)
        except Exception as e:
            # print(e)
            pass

    likelihooddict = {}

    for i in data:
        
        if i.likelihood not in likelihooddict:
            if i.likelihood != "":
                likelihooddict[i.likelihood] = 1
        else:
            likelihooddict[i.likelihood] +=1
    
    relevancedict = {}

    for i in data:
        
        if i.relevance not in relevancedict:
            if i.relevance != "":
                relevancedict[i.relevance] = 1
        else:
            relevancedict[i.relevance] +=1


    topicdict = {}
    for i in data:
        if i.topic not in topicdict:
            if i.topic != "":
                topicdict[i.topic] = 1
        else:
            topicdict[i.topic] +=1



    topfivetopics = sorted(topicdict, key=topicdict.get, reverse = True)[:5]
    toptopicdict = {}

    for i in topfivetopics:
        toptopicdict[i] = topicdict[i]
    
    countrydict = {}

    for i in data:
        
        if i.country not in countrydict:
            if i.country != "":
                countrydict[i.country] = 1
        else:
            countrydict[i.country] +=1
        

    topcountrylist = sorted(countrydict ,key=countrydict.get , reverse=True)[:10]
    topcountrydict = {}

    for i in topcountrylist:
        topcountrydict[i] = countrydict[i]


    parms ={
        "data":data,
        "intensitydict":intensitydict,
        "likelihooddict":likelihooddict,
        "relevancedict":relevancedict,
        "topic":toptopicdict,
        "country" :topcountrydict,

        "end_year_filter":end_year_filter,
        "topic_filter": topic_filter,
        "region_filter": region_filter,
        "source_filter": source_filter,
        "sector_filter": sector_filter,
        "country_filter": country_filter,
    }

    return render(request, "home/dashboard.html",parms )


