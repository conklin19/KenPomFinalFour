# KenPomFinalFour
Analyzing KenPom data for NCAA Men's 

This project involves importing data from kenpom.com, from Ken Pomeroy. This is a marquee advanced data analytic for college basketball that is often used to set sports
betting lines for both spread (how much a team could win by) and the total (combined points scored by both teams). The KenPom data goes back to 2002. I have imported the data for teams that made the NCAA Men's Basketball Tournament Final Four from 2002 - 2021 (I deleted 2020 because there was no tournament due to COVID-19)


See requirements.txt for full requirements (python, pandas, matplotlib, numpy)

I read in the .csv using pandas and called it df

For testing purposes, I wanted to copy the dataframe. I copied df and called if FFdata.

Example Row: [Year, Team, KPrank, KPvalue, Conference, Champion]

Year = calendar year from 2002 - 2021 (except 2020)
Team = the team that made the Final Four
KPrank = the overall rank for each Final Four team per KenPom
KPvalue = the kenpom rating for each Final Four team
Conference = the conference that team plays in
Champion = if the team won the national championship. 1 means they won the championship, 0 means they did not win the championship

I used != to delete the rows for the year 2020 because there was no tournament due to COVID-19

I created a dictionary to relate the conference abbreviation to the full name (B10 = Big Ten, COL = Colonial)

Created a dataframe from FFdata that includes ONLY the national champions

Line 43 I found the highest rated kenpom team that made that Final Four (Kentucky 2015)

Line 50 - performed basic calcuations on KenPom rank for the Final Four teams

Line 88- Plotted KenPom Rank and KenPom Value per year via matplot lib

I found the average KenPom rank for an NCAA Final Four team to be 7.85. The standard deviation is just under 9, so most you can assume most teams that make the
Final Four will have a KenPom rank from 1 to around 17. This reinforces KenPom as a standard bearer for analyzing top College Basketball Teams. 
