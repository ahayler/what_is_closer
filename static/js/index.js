// declares the necceary variables
var tmp;
var score = 0;
var city_a;
var city_b;
var loc;
var coordinates;
var button_a = document.querySelector('#button_a');
var button_b = document.querySelector('#button_b');
var button_next = document.querySelector('#button_next');


// called when the document is fully loaded
$(document).ready(function(){
    
    // displays your score
    score_update();
    
    
    // gets your current location data and displays it
    $.get("https://ipinfo.io/json", function(response) {
        
        loc = response;
        coordinates = loc.loc.split(',');
        console.log(response);
        document.querySelector('.x').innerHTML = (loc.city) + ", " + (loc.region) + ", " + (loc.country) + " (lat: " + coordinates[0] + ", lng: " + coordinates[1] + ")";
        
    });
    
    // request and inserts the start data
    update();
    
        
    // loads the next round if the next_button is clicked  
    button_next.onclick = function(){
        update();
        
    };
    // calls check with the right data if button_a was clicked    
    button_a.onclick = function(){
        check(city_a, city_b, "normal");
        
    };
    
    // calls check with the right data if button_ab was clicked    
    button_b.onclick = function(){
        check(city_b, city_a, "reverse");
        
    };
    
    
    
    // declaring necessary functions
    function check(choosen_city, other_city, order){
        $.get('/check?loc_lat=' + coordinates[0] + '&loc_lng=' +  coordinates[1]
              + '&c_city_lat=' + choosen_city.lat + '&c_city_lng=' + choosen_city.lng
              + '&o_city_lat=' + other_city.lat + '&o_city_lng=' + other_city.lng
              + '&order=' + order, function(data) {
            // adjusts the website according to the results
            // displays if you were right or wrong
            if (data["result"]){
                document.querySelector('#result').innerHTML = "You were right!";
                score += 1;
            }
            else {
                document.querySelector('#result').innerHTML = "You were wrong!";
                document.getElementById('hiddenField').value = score;
                tmp = score;
                score = 0;
                
                // adjusts the form header
                document.querySelector('#form_header').innerHTML = "Submit your score of " + tmp + " to the leaderboard";
                
                // displays the form
                document.querySelector('form').style.display = "block";
            }
            
            // updates the score
            score_update();
            
            // displays the city-data
            // inserts the HTML
            document.querySelector('#city_a_data').innerHTML = "Distance: " + data.dist_a + ' (lat: ' + city_a.lat + ' lng: ' + city_a.lng + ')';
            document.querySelector('#city_b_data').innerHTML = "Distance: " + data.dist_b + ' (lat: ' + city_b.lat + ' lng: ' + city_b.lng + ')';
            
            // changes the content of the next round button according to the score
            if(score != 0)
            {
                document.querySelector('#button_next').innerHTML = "Next round";
            } 
            else
            {
                document.querySelector('#button_next').innerHTML = "Start new game";
            }
            // unhides the data and the next-round.button
            document.querySelector('#city_a_data').style.display = "block";
            document.querySelector('#city_b_data').style.display = "block";
            
            document.querySelector('#button_next').style.display = "block";
            document.querySelector('#result').style.display = "block";
            
                    
            // hides the buttons of city a and b
            document.querySelector('#button_a').style.display = "none";
            document.querySelector('#button_b').style.display = "none";
        });
    }
    
    function update (){
    // gets and inserts the two cities
    $.get('/update', function (data){
        // saves the data  
        city_a = data[0];
        city_b = data[1];
        
        // displays the city
        document.querySelector('#city_a').innerHTML = (city_a.city_ascii) + ', ' + (city_a.country);
        document.querySelector('#city_b').innerHTML = (city_b.city_ascii) + ', ' + (city_b.country);
        
        // hides the additonal data and the next_round_button and the form and the results
        document.querySelector('#city_a_data').style.display = "none";
        document.querySelector('#city_b_data').style.display = "none";
        
        document.querySelector('#button_next').style.display = "none";
        document.querySelector('#result').style.display = "none";
        
        document.querySelector('form').style.display = "none";
        
        // shows the buttons of city a and b
        document.querySelector('#button_a').style.display = "inline-block";
        document.querySelector('#button_b').style.display = "inline-block";
        
        });
    };
    
    function score_update (){
        document.querySelector('#score').innerHTML = score;
    }
    
});