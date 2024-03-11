# <font color="Brown"> <center> BOOK RECOMMENDATION SYSTEMS </font>

<img src="https://t3.ftcdn.net/jpg/05/65/35/08/360_F_565350821_t9oAsB34PziL8lDGl7ZHq0QFhbgqNKkL.jpg" alt="your image" width="1000" height="500"></img>

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

2. Content Based Recommender System:
Content-Based Filtering recommends items by analyzing the attributes of the items and the user's preferences. In a music
streaming service like Spotify, content-based filtering could recommend songs based on the genre, artist, or mood of the songs
the user has previously enjoyed. If a user often listens to pop songs, the system might suggest other pop songs with similar
characteristics.



3. Collaborative Filtering Based Recommender Sytems:
Collaborative Filtering recommends items based on the preferences and behavior of users with similar tastes. It relies on the
assumption that users who liked similar items in the past will continue to do so in the future. Example: Collaborative Filtering
recommends items based on the preferences and behavior of users with similar tastes. It relies on the assumption that users who
liked similar items in the past will continue to do so in the future.


4. Hybrid Recommender Systems:
Hybrid Recommender Systems combine collaborative filtering and content-based filtering to leverage the strengths of both
approaches. Examples: An e-commerce platform like Amazon utilizes a hybrid recommender system. It considers collaborative
filtering by suggesting products that other users with similar purchase histories have bought. Additionally, it employs contentbased filtering by recommending items based on the specific attributes and features of products a user has previously viewed or
purchased.


