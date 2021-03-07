d3.json("static/data/resume.json", function (data) {
    var sections = Object.keys(data).slice(1);
    
    d3.selectAll("section")
        .data(sections)
        .enter()
        .append("section")
        .attr("id", d => d[0]);
    
})