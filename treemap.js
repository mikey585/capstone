$(document).ready(function() {
    treemap();
});

function treemap() {
  var margin = {top: 40, right: 10, bottom: 10, left: 10},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

  var color = d3.scale.category20c();

  var treemap = d3.layout.treemap()
    .size([width, height])
    .sticky(true)
    .value(function(d) { return d.size; });

    var div = d3.select("body").append("div")
        .style("position", "relative")
        .style("width", (width + margin.left + margin.right) + "px")
        .style("height", (height + margin.top + margin.bottom) + "px")
        .style("left", margin.left + "px")
        .style("top", margin.top + "px")
        .style("margin", "auto");

        d3.json("json_result2.json", function(error, root) {
        if (error) throw error;

        var node = div.datum(root).selectAll(".node")
            .data(treemap.nodes)
          .enter().append("div")
            .attr("class", "node")
            .call(position)
            .style("background", function(d) { return d.children ? color(d.news_desk) : null; })
            .text(function(d) { return d.children ? null : d.name; })
            .on("mouseover", function(d){
                $(this).css('cursor','pointer')})
            .on("click", function(d){
                window.open(d.link)});

        d3.selectAll("input").on("change", function change() {
          var value = this.value === "count"
              ? function() { return 1; }
              : function(d) { return d.size; };

          node
              .data(treemap.value(value).nodes)
            .transition()
              .duration(1500)
              .call(position);
        });
      });

      function position() {
        this.style("left", function(d) { return d.x + "px"; })
            .style("top", function(d) { return d.y + "px"; })
            .style("width", function(d) { return Math.max(0, d.dx - 1) + "px"; })
            .style("height", function(d) { return Math.max(0, d.dy - 1) + "px"; });
      }

  // var color = d3.scale.category10();
  //
  // var canvas = d3.select("#treemap").append("svg")
  // .attr("width", 500)
  // .attr("height", 500);
  //
  //
  // d3.json("mydata.json", function (data) {
  //   var treemap = d3.layout.treemap()
  //   .size(500, 500)
  //   .nodes(data);
  //
  //   console.log(data)
  //
  //   var cells = canvas.selectAll(".cell")
  //   .data(treemap)
  //   .enter()
  //   .append("g")
  //   .attr("class", "cell");
  //
  //   cells.append("rect")
  //   .attr("x", function(d) { return d.x; })
  //   .attr("y", function(d) { return d.y; })
  //   .attr("width", function(d) { return d.dx; })
  //   .attr("height", function(d) { return d.dy; })
  //   .attr("fill", function(d) { return d.children ? null : color(d.parent.name); })
  //   .attr("stroke", "#fff");
  //
  //   cells.append("text")
  //   .attr("x", function(d) { return d.x + d.dx / 2})
  //   .attr("y", function(d) { return d.y + d.dy / 2})
  //   .text(function(d) {return d.children ? null : d.name; });
  // });
}
