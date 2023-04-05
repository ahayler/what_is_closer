**Final Project: What is closer? - The Game**

This is was my final project for CS50's Introduction to Computer Science. Quoting from the in-game-instructions:

_"The Website gives you each round two random cities from all around the world. You then have to guess what city is closer to your geographic location
(You can see your location at the top of the website). Keep guessing correctly and increase your score. In the end you can submit your score to the online 
leaderboard to compete with other players."_

It is build with a database consisting of two SQL tables (one a dataset of 12k cities from simplemaps.com and the other one is the leaderboard).
A big part of the game is run on the clientside using Javascript. This is done for the following reasons:
1. I really wanted to get comfortable with JS in the final project, because it was my main point of struggle during the course
2. JS enabled me to minimize server traffic and enabled a smooth expericence on the client side
3. JS made the website more interactive

The distances are calculated by the geopy libary in Pyhton, because calculating accurate distances is else quite hard (as the earth is not a perfect sphere).
Here a link to a short video showing my project: https://www.youtube.com/watch?v=WX_3DsI_fSg&ab_channel=AdrianH.
