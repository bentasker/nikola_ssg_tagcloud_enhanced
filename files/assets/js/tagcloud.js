async function buildTagCloud(multiplier){
    var response = await fetch('/assets/js/tag_cloud_data_enhanced.json');
    
    response.json()
    .then(tags => {
        var k, v, weight, perc, style, li, a;
        var wrapper = document.getElementById('tag-cloud-wrap');
        if (!wrapper){
            return;
        }
    
        var hBound = false;
        var lBound = false;
    
        // Calculate the bounds
        for ([k, v] of Object.entries(tags)){
            weight = v[0];
            
            if (!hBound || weight > hBound){
                hBound = weight;
            }

            if (!lBound || weight < lBound){
                lBound = weight;
            }
        }
               
        // Insert the tags, applying weighting
        for ([k, v] of Object.entries(tags)){
            weight = v[0];
            
            // Calculate the size to use as a percentage
            perc = Math.abs((weight - lBound) / (lBound - hBound));
            
            style = "font-size: " + (1 + (perc * multiplier)) + "em";
            
            li = document.createElement('li');
            li.className = "tagCloudEle";
            li.style = style;
            
            a = document.createElement('a');
            a.innerText = k;
            a.href = v[1];
            
            li.appendChild(a);
            wrapper.appendChild(li);
        }
        
        // Add a title
        h3 = document.createElement('h3');
        h3.innerText = "Tag Cloud";
        wrapper.parentNode.insertBefore(h3, wrapper);
    });
}
