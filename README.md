# <font color="Brown"> <center> BOOK RECOMMENDATION SYSTEMS </font>

<img src="https://t3.ftcdn.net/jpg/05/65/35/08/360_F_565350821_t9oAsB34PziL8lDGl7ZHq0QFhbgqNKkL.jpg" alt="your image" width="1000" height="200"></img>

- In the contemporary era of advanced technology and modern mobile devices, there is a growing concern that these digital
distractions may be adversely impacting our reading skills and imagination. The pervasive use of smartphones and tablets
often leads individuals to engage in shorter attention spans and reduced focus on in-depth reading experiences. In this
context, the problem statement arises: How can we encourage a return to the timeless practice of reading books, even in
2024, while preserving the enriching and imagination-stimulating qualities associated with traditional, old-school reading?
The challenge lies in developing a book recommendation system that not only promotes the accessibility of literature but
also strategically curates recommendations to evoke the charm of classic reading experiences, fostering a reconnection with
the profound benefits of extended and immersive storytelling.

## Approach
- Our plan of action is very simple, there are popular books, we have read atleast any one of those. We might liked them as well, so
we are going to build a recommender system, which recommends similar type or genre of books which you liked it earlier.
We are going to collect the dataset from open source i,e kaggle, perform cleaning, analyzing and performing EDA.
we are going to use the cosine simiarity to get eucledian distance of every vector. cosine similarity identifies closest vectors by 0
to 1.

## What is a Recommender System?
**Before jumping into work, first let's understand what is a recommender system, it's types and how it works.**
- The system which recommends items according to user preference.
Example:- A shopkeeper in a clothes shop, who recommends clothes to customers based on user preference. His Recomendations
must be so good that makes customer purchase the items.

**Types of Recommender Systems :**
1. Popularity Based Recommnder System:
A popularity-based recommender system is a simple recommendation approach that suggests items based on their overall
popularity or frequency of selection among users. Example : Youtube, IMDB top 250 movies. "Best Sellers" or "Top Rated"
Sections on Amazon
<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_EzZM085Lnt6f6l1rsrLpFv8Ptp67DK5UsHyJ7YAJLPIeJ_6rnRcu8oy257Z7xf2xZS6iYmerpGoghyyZ70p8jCDD20Wy6fkPDlp0ta4IoklGD6Z90yrlYaL_T--e1YL42OrKVtMvEjDbx2PsoUYhn2jwYp56PqPmXT66Y4FNgcksKAK63C5OAeO6fQ/s1280/popularity%20based%20recommendation%20system.png" alt="your image" width="200" height="200"></img>

2. Content Based Recommender System:
Content-Based Filtering recommends items by analyzing the attributes of the items and the user's preferences. In a music
streaming service like Spotify, content-based filtering could recommend songs based on the genre, artist, or mood of the songs
the user has previously enjoyed. If a user often listens to pop songs, the system might suggest other pop songs with similar
characteristics.

<img src="[[https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_EzZM085Lnt6f6l1rsrLpFv8Ptp67DK5UsHyJ7YAJLPIeJ_6rnRcu8oy257Z7xf2xZS6iYmerpGoghyyZ70p8jCDD20Wy6fkPDlp0ta4IoklGD6Z90yrlYaL_T--e1YL42OrKVtMvEjDbx2PsoUYhn2jwYp56PqPmXT66Y4FNgcksKAK63C5OAeO6fQ/s1280/popularity%20based%20recommendation%20system.png](https://www.nvidia.com/content/dam/en-zz/Solutions/glossary/data-science/recommendation-system/img-2.png)](https://media.geeksforgeeks.org/wp-content/uploads/20200501010023/my4.png)" alt="your image" width="200" height="200"></img>


3. Collaborative Filtering Based Recommender Sytems:
Collaborative Filtering recommends items based on the preferences and behavior of users with similar tastes. It relies on the
assumption that users who liked similar items in the past will continue to do so in the future. Example: Collaborative Filtering
recommends items based on the preferences and behavior of users with similar tastes. It relies on the assumption that users who
liked similar items in the past will continue to do so in the future.

<img src="[https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_EzZM085Lnt6f6l1rsrLpFv8Ptp67DK5UsHyJ7YAJLPIeJ_6rnRcu8oy257Z7xf2xZS6iYmerpGoghyyZ70p8jCDD20Wy6fkPDlp0ta4IoklGD6Z90yrlYaL_T--e1YL42OrKVtMvEjDbx2PsoUYhn2jwYp56PqPmXT66Y4FNgcksKAK63C5OAeO6fQ/s1280/popularity%20based%20recommendation%20system.png](https://www.nvidia.com/content/dam/en-zz/Solutions/glossary/data-science/recommendation-system/img-2.png)" alt="your image" width="200" height="200"></img>


4. Hybrid Recommender Systems:
Hybrid Recommender Systems combine collaborative filtering and content-based filtering to leverage the strengths of both
approaches. Examples: An e-commerce platform like Amazon utilizes a hybrid recommender system. It considers collaborative
filtering by suggesting products that other users with similar purchase histories have bought. Additionally, it employs contentbased filtering by recommending items based on the specific attributes and features of products a user has previously viewed or
purchased.

<img src[="[https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_EzZM085Lnt6f6l1rsrLpFv8Ptp67DK5UsHyJ7YAJLPIeJ_6rnRcu8oy257Z7xf2xZS6iYmerpGoghyyZ70p8jCDD20Wy6fkPDlp0ta4IoklGD6Z90yrlYaL_T--e1YL42OrKVtMvEjDbx2PsoUYhn2jwYp56PqPmXT66Y4FNgcksKAK63C5OAeO6fQ/s1280/popularity%20based%20recommendation%20system.png](https://www.nvidia.com/content/dam/en-zz/Solutions/glossary/data-science/recommendation-system/img-2.png)"](https://www.researchgate.net/profile/Xiangjie-Kong-2/publication/330077673/figure/fig5/AS:710433577107459@1546391972632/A-hybrid-paper-recommendation-system.png)https://www.researchgate.net/profile/Xiangjie-Kong-2/publication/330077673/figure/fig5/AS:710433577107459@1546391972632/A-hybrid-paper-recommendation-system.png alt="your image" width="200" height="200"></img>

