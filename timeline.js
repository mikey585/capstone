$(document).ready(function() {
    var submit = document.getElementById("search_button");
    submit.onclick = getResult;
});

var timelineEvents = [
      ];

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

// var timelineEvents = [{
//   name: "In China, Diners Pay for Clean Air With Their Entree",
//   date: "2015-12-15",
//   img: "http://static01.nyt.com/images/2015/12/16/world/16chinaair/16chinaair-master675.jpg"
// }, {
//   name: "Morning Agenda: A New Global Currency War",
//   date: "2015-08-14",
//   img: ""
// }, {
//   name: "Russia Expands Sanctions Against Turkey After Downing of Jet",
//   date: "2015-12-30",
//   img: "http://static01.nyt.com/images/2015/12/31/world/31RUSSIA-web2/31RUSSIA-web2-articleLarge.jpg"
// }, {
//   name: "Greece Flashes Warning Signals About Its Debt",
//   date: "2015-04-19",
//   img: "http://static01.nyt.com/images/2015/04/20/business/GREEKDEBT/GREEKDEBT-master675.jpg"
// }, {
//   name: "Paris Attack Updates, Day 3: Two Hostage Situations",
//   date: "2015-01-09",
//   img: "https://pbs.twimg.com/media/B67VKs7IQAAZ4yz.jpg"
// }, {
//   name: "‘Jurassic World’ Tromps All Over the Box Office Competition",
//   date: "2015-05-14",
//   img: "http://static01.nyt.com/images/2015/06/15/arts/BOXOFFICE/BOXOFFICE-master675.jpg"
// }];
