# Mini-project IV

### [Assignment](assignment.md)

## <u>Table of Contents</u>
- [Main Notebook](/notebooks/instructions.ipynb)
- [Presentation PDF](/images/Deployment_Slides.pdf)
- [Modules Folder](/notebooks/modules/)
    - [Evaluation Module](/notebooks/modules/eval.py)
    - [Cleaning Module](/notebooks/modules/cleaning.py)
- [Output](/src/)
    - [API script](/src/app.py)
    - [Website script](/src/website.py)

## <u>Project/Goals</u>
In this project we're building and deploying a loan eligibility estimator based on demographic.

I want to get more familiar with the bridge between backend and frontend development and expirement with Streamlit.

## <u>Hypothesis</u>
I know that people with healthy responsible credit history, good consistent income, few deliquencies and inquiries, lower utilization, and high available credit **get the best loans.**

I think people with **higher income and education** will have the highest correlation to these stats being in a positive state. However it's obviously not perfectly linear. Anyone can pop or misuse / misunderstand a credit card, go bankrupt, be in between jobs / less than 3 months on the job.

**This hypothesis can be tested** by doing EDA, pivot tables are especially handy, we can also check the feature importance in our model, do some PCA and see what the heaviest features in the first x PCs are, use a for loop to try a bunch of predictions on our model incrementing / changing two or three features and plot them coloring by the decision.

## <u>EDA </u>
**There's lots of biased data** but since it's not too extreme and we're predicting loan eligibility by the demographic we think they belong to and not by their individual attributes we're going to leave it in. For example ~69% of men get approved and ~67% of females get approved, this will produce bias, but not a bias that's too strong. The gap in Education is much more significant at ~20% so our model will be biased against the uneducated like myself but again I don't think this is unjust because if you're uneducated statistically you have lower income, less financial knowledge, and overall more trouble with approvals. I could go on about bias for a while but I hope you see the point.

The **data seems to be collected from around the same area** which is likely not around a 'hotspot' in the country like Vancouver or Toronto. The mean loan amount is 145k. Over here on Vancouver Island I'm not sure a real estate agent would shake my hand for 145k.

An interesting discovery is unlike females, males who are approved have on average lower income than men who aren't approved. **This implies an interesting pattern of financial irresponsibility** in higher earning males. It's possible this comes from scenarios like the oil industry. Anyone can work on an oil patch and make six figures and ~90% are male and 100% of the men I've met working high paying labour jobs in oil don't spend that money responsibly. I've met a decent amount of high earning men I haven't been able to get approved due to a poor understanding and/or use of credit.

Another thing is **self employment.** This is a very important question as self employment and loans for incorporated entities is a tricky and polarizing side of banking. If we knew how long each person had been self employed for it would greatly help our predictions. There's many factors in self employment like how they're paying themselves, how long they've been afloat, and how consistent their income is. A lot of times self employed or incorporated entities will want to get loans for assets early on and will have a very hard time getting even a small loan because they don't have solid income yet or solid, if any, credit. These same people/entities years later can take out massive loans without sweating through the same lenders that rejected them before. This creates a very polarizing landscape where on one side they're struggling to get a $50k loan and on the other side they're effortlessly taking out $5M loans and rapidly acruing assets increasing their available credit.

People without coapplicants have a **higher chance of getting approved**. This makes sense because if you're being sent out alone either your credit is pretty good or you have no connections/people who are willing to go on a loan with you. The latter isn't too common.

## <u>Process</u>
- For **EDA** I explored the data concisely using lots of subplots and some verbal stats.
- for **cleaning** I made a [cleaning module](/notebooks/modules/cleaning.py) to fill all values in a way that's most appropriate to each column
- I also investigated and addressed other concerns like multiple dtypes in columns
- We can drop columns like Gender and Education as they aren't needed but I'm going to keep them in as they aren't that important to our model and the focus here is more on deployment. **If this was a real model and a real deployment I would 100% drop them though.** Then I would just collect the gender and whatever else and not process it but just include it in the generated lead. Cold calls are hard and any information helps!
- For **feature engineering and modeling** I didn't do anything too crazy because my focus with this project was more so deployment
- With that being said I did run two grid searches on my xgboost model and compared the results before and after using 'print_scores()' from my [evaluation module](/notebooks/modules/eval.py)
- The first grid search explored broad values and the second explored a finer range of values centered on the chosen values from the first grid search.
- For **deployment** I first had to build my pipeline.
- Then I built the website and api on my computer so I could quickly and easily visualize and tweak it from the comfort of my own environment.
- Once everything was how I wanted it I **moved it onto the cloud and deployed it** in a new tmux session to run indefinetly.

## <u>Results/Demo</u>
(fill in your model's performance, details about the API you created, and (optional) a link to an live demo)

The model performed as **good as it had to for the use case I chose**. It had more false positives than false negatives which I like because discouraging/pushing away someone who can and will buy something is worse than encouraging someone who can't.

At the bottom of my [instructions notebook](/notebooks/instructions.ipynb) there's an **example usage of the API and screenshots of the website.**

**Regarding the live demo,** I'm not familiar with AWS security and best practices so I'm not going to push the public ip of my AWS instance to a public github for the same reason I'm not going to push an API key to a public github.

## <u>Challenges</u>
Even though I thought I was being very careful and thoughtful in my move from Windows to **Linux there were a lot of issues and time spent troubleshooting.** I found a ton of weird issues where the developer of a package would say it's more a problem with the specific Python version than with their package so they don't want to fix it to just change to a very slightly different version of Python. Changing versions of tons of stuff including the C++ runtime while trying to keep compatibility when working with a very limited amount of storage on my instance was very tricky. I also thought that package versions would be pretty uniform across each OS but instead found that there were some packages that seemed to have stopped being ported to Linux.

The next time I have to do this I'm going to take another approach for sure. I'll likely use Docker despite hearing very little positive about it including my friend saying it bricked his school laptop and behaves like bloatware. My experience with the little bit of docker I've used so far is very similiar to my time with Ubuntu on AWS in that it's also riddled with bugs that people and developers just cope with / workaround instead of fixing. **However if using it negates the issues I ran into and ultimately saves time it sounds like a nescessary evil.**

## <u>Future Goals</u>
- Explore the capabilities of streamlit further. Explore a package for sending emails to actually generate these mock leads.
- Experiment with neural networks.
- Learn how to deploy on custom domains.