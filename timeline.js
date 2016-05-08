$(document).ready(function() {
    var submit = document.getElementById("search_button");
});

var timelineEvents = [];

function getResult() {

    var search = parseInt(document.getElementById("search").value);
    for (var month = 1; month < 13; month++){
        var day = Math.floor((Math.random() * 28) + 1)
        url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?[q=%20&begin_date=" + search +
        ("0" + month).slice(-2) + ("0" + day).slice(-2) + "&end_date=" + search +
        ("0" + month).slice(-2) + ("0" + day).slice(-2) + "&]&api-key=93fc659744f5238f6f95d464865562b8:16:74068039"
        //articles are being pulled too fast and cause an error if we don't add a delay. alerts mimic this behaviour.
        $.getJSON(url, function(result){
            timelineEvents.push({name : result.response.docs[0].snippet,
                date : result.response.docs[0].pub_date,
                link : result.response.docs[0].web_url
            });
            //alert(result.response.docs[0].web_url)
        });
        //alert(month);
    }
    //alert("for loop out")
    var delay=1000; //1 seconds

setTimeout(function(){
    $.getJSON(url, function(result){
        //alert("drawTimeline")
        drawTimeline();
        timelineEvents = [];
    })
}, delay)}

function checkInp()
{
  var x=document.getElementById("search").value;
  if (isNaN(x) || x < 1995 || x > 2015)
  {
    alert("Input a valid year: 1995-2015");
    return false;
  }
}

function drawTimeline() {
   TimeKnots.draw("#timeline", timelineEvents, {
          dateFormat: "%H:%M:%S %d %B %Y",
          color: "#696",
          width: 1000,
          showLabels: true,
          labelFormat: "%Y"
        });
  console.log(timelineEvents);
}
