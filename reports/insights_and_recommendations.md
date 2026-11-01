# Netflix: Data Exploration & Visualisation: Insights and Recommendations

*Guntuku Hariprasad · 8,807 Netflix titles (catalogue up to 25 Sep 2021) · full analysis in `notebooks/Netflix_EDA_Case_Study.ipynb`*

## Problem statement
Analyse the Netflix catalogue to recommend **which type of shows and movies Netflix should produce** and **how it can grow the business in different countries**.

## Basic metrics & data quality
- 8,807 titles × 12 columns; 69.6% movies (6,131), 30.4% TV shows (2,676). No duplicate rows or IDs.
- Release years 1925–2021 (median 2017; 84.8% released 2010 or later). Added to Netflix Jan 2008 – Sep 2021.
- Missing: director 29.9% (91% of TV shows have no director, which is structural), cast 9.4%, country 9.4%, date_added 0.1%, rating 0.1%. Filled with "Unknown"; no rows dropped.
- 3 rows had duration typed into the rating column (Louis C.K. specials); fixed.
- Categorical columns (type, rating, audience, duration unit, weekday) converted to `category`.
- After un-nesting: 122 countries, 42 genres, 36,439 actors, 4,993 directors; 1,315 titles (15%) are multi-country co-productions.

## EDA insights
**Range & distribution**
- Movie duration: 3–312 min, near-normal around a median of 98 min (middle 50%: 87–114). 450 IQR outliers (stand-up/shorts and long Indian epics), kept as genuine.
- TV seasons: 1–17, extremely right-skewed; 67% have one season, only ~9% have 4+.
- Release year is left-skewed (peak 2017–18); TV is newer (median 2018) than movies (2016).
- Ratings: TV-MA 36.4%, TV-14 24.5%. Audience: Adults 45.6%, Teens 30.1%, Older Kids 16.9%, Little Kids 6.5%.

**Relationships**
- TV share of yearly additions: 41% (2016) → 25% (2018) → 29% → 32% → 34% (2021).
- Titles released in 2021: 315 TV shows vs 277 movies. Movies peaked with 2017–18 releases; TV grew until 2020.
- Additions peaked at 2,016 in 2019; movies fell 10% in 2020 while TV stayed flat (592 → 595).
- Movie duration rises with audience age: TV-Y 46 min → PG-13 106, TV-14 107 min. Stand-up (65), documentaries (86) and kids' films (87) are shortest; dramas (109) and action (108) longest.
- Newer movies are shorter (median ~112–118 min for 1970s–80s films vs ~95 min since 2015; correlation −0.21).
- TV reaches Netflix in its release year (median 0 years); movies after ~2 years, consistent with originals vs licensing.
- Country × type: India 92% movies; Japan 63% TV; South Korea 74% TV; UK 34% TV; US 25% TV.
- Country × genre: US most balanced (docs 11%, kids/family 8%); India 73% international movies + dramas + comedies; Japan highest action share (anime); Korea 40% international TV; Canada highest kids' share (12% family movies, 9% kids' TV); Mexico/Spain over-index on crime TV and thrillers.
- Country growth 2018→2020: India 349 → 199 (−43%); Japan 44 → 79; South Korea 33 → 56; Nigeria 1 → 42; Egypt 3 → 54 (but only 7 in 2021).
- Genre growth 2018→2020: Children & Family Movies +100%, Reality TV +95%, Kids' TV +66%, Romantic Movies +60%; Stand-Up −46%, Documentaries −29%.
- Timing: 28% of titles (35% of TV shows) added on a Friday; 2,212 titles on the 1st of a month; TV peaks in December and July, February is weakest.
- People: top movie actors are Indian (Anupam Kher 42, Shah Rukh Khan 35, Naseeruddin Shah 32); top TV actors are Japanese anime voice actors (Takahiro Sakurai 25, Yuki Kaji 19); top movie directors are Rajiv Chilaka (22), Jan Suter (21), Raúl Campos (19). TV directors rarely exceed 2–3 titles.

## Business insights
1. Netflix is pivoting to TV: rising TV share of additions, and TV now outnumbers movies among the newest releases.
2. Content growth has plateaued since 2019, so future gains must come from better targeting, not more volume.
3. The library is adult-first, and the fastest-growing genres are kids/family and reality, a gap Netflix is already filling.
4. International content is the brand's core; each market has a distinct format and genre "personality".
5. Most shows are cancelled or end after one season, which signals heavy experimentation.
6. Release timing is deliberate: Fridays, 1st of the month, July and December.

## Recommendations
1. **Make more TV series**, especially international dramas, crime and kids' shows.
2. **Renew good shows**: two in three stop after season 1, so set clear rules to give finished-and-loved shows a second season.
3. **Grow family and kids' content**: only 1 in 15 titles is for little kids, yet it is one of the fastest-growing areas. Use proven animation hubs (India, Canada).
4. **Go local:** Indian movies with local stars, plus Indian web-series; anime from Japan; K-dramas and romance from Korea; Spanish-language crime and thrillers from Mexico and Spain; partner with local studios in fast-growing Nigeria and Egypt.
5. **Keep movies at 90–110 minutes**; kids' movies can be around an hour.
6. **Launch big shows on a Friday, in July or December**; keep February for smaller titles.
7. **Invest in growing genres** (reality, romance, action, kids); spend carefully on stand-up and documentaries.
8. **Co-produce to enter new countries**, which lowers cost and risk.
9. **Add well-known classic films selectively** to attract older viewers cheaply.
10. **Track what people watch**, not just what is added, and review these bets every quarter.
