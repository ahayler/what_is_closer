Final Project: What is closer? - The Game

My final project is a simple browser game. Quoting from the in-game-instructions:
"The Website gives you each round two random cities from all around the world. You then have to guess what city is closer to your geographic location
(You can see your location at the top of the website). Keep guessing correctly and increase your score. In the end you can submit your score to the online 
leaderboard to compete with players all around the world."

It is build with a database consisting of two tables (one a dataset of 12k cities from simplemaps.com and the other is the leaderboard).
A lot of the game is run on the clientside with Javascript. This is done because of the following reasons:
1. I really wanted to get comfortable with JS in the final project because it was my main point of struggle during pset8
2. JS enables me to minimize server traffic and enables a smoth expericence on the client side
3. JS makes the website more interactive

The distances are calculated by the geopy libary in pyhton, because getting very accurate distances is else very hard (as the earth is in reality no sphere).

The Webapp features 3 html-pages in total (the game itself, the leaderboard and instructions):