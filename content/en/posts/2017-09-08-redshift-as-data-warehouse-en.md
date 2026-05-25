---
title: "Data Warehouse Solution: A Guide to Getting Started with RedShift"
date: "2017-09-08 22:59:08"
zhUrl: /redshift-as-data-warehouse
aliases:
  - /redshift-as-data-warehouse-en
---

Recently engineer Little Xie ran into a tough problem,
which is he has tens of millions of records on hand,
but no quick-rough-strong solution.

<!--more-->

## Stating the Problem

> Want to read directly about RedShift,
> please skip the first two sections of BS.
> Jump straight to section 3.

Unlike that small number of outstanding people who can live on the other shore,
who can pour their heart into writing perfect databases,
learning all programming languages in a flash;
most programmers in the world live on this shore,
they solve specific business problems one by one.

Engineer Little Xie was troubled,
[last time product manager Little Liu raised a super cool IDEA:][cash-cow]
"Cash Cow".
The audience was thrilled,
but as the person who has to implement the feature,
Little Xie was a bit gloomy.

Specifically, the difficulties are these:

1. Big data volume.
The company is about dishes, the dish data recorded daily is enormous.
And as the company's business develops, the dish growth rate is also high.
(That is, "exponentially rising")

2. Tight timeline.
Unlike school's big assignments, where you can have a whole semester to implement and deliver.
Real requirements need to be completed as early as possible, even if it's not perfect at first,
but you'll get external feedback earlier, positive/negative evaluations help everyone adjust direction forward.

3. Quality requirements.
After "Cash Cow"'s requirement is delivered, new requirements will descend on Little Xie's shoulders.
So this current solution also needs to solve future problems.
As business/data volume grows, in short term (say, a year), the solution must be stable and reliable.
In the long term (say, three years), the solution must be extensible, at least easy to refactor.


## Solution

The few problems above
are actually just like thousands of real-world problems,
they're all one problem: `How to accomplish defined goals under limited resources?`
The solutions are also universal: `convert resources, spend time, change goals`.

Of course, Little Xie understands, methodology divorced from concrete examples has no meaning.
So Little Xie planned to set up a data warehouse (Data Warehouse).

Data warehouse, very similar to database (DataBase),
just like an armory is where weapons are placed,
a garage is where cars are placed,
data warehouse / database is where data is placed.
~~The extra "warehouse" is because hamsters are also placed there~~

The detailed differences between the two are because the problems they solve are different:
databases provide basic guarantees for business,
data warehouses provide convenience for decision-oriented data analysis;
so the two have different design thinking:
databases follow normalization design, emphasize data constraints, consistency, both read and write operations involved,
data warehouses store large amounts of redundant data, statistical data, optimized more for reading.

**For example** today at lunch Little Xie went to eat four jin of grilled fish (really can eat),
"four jin of grilled fish" data exists in the database, used to settle the bill.
But "today at lunch, four jin, grilled fish" this statistical data exists in the data warehouse,
to be used for later statistical analysis.

Most industry data warehouses are based on a `Hadoop/Spark/Storm` set of `Java`-stack tech.
For example Pinduoduo uses the `Hadoop/Hive/HBase/Kafka` tech stack.
For example Xiaohongshu uses the `Hadoop/Hive/Spark/Kafka` tech stack.

But there's a problem:
Little Xie doesn't understand any of this, very awkward.
Fortunately, Little Xie has money,
he can hire a few who understand.
Unfortunately, hiring is a mystical problem,
those he likes don't like him,
those who like him he doesn't like.

So Little Xie thought it over,
could only do it himself,
ultimately choosing:


## RedShift, the Data Warehouse Management Assistant in Amazon's Cloud Services Family Bucket


### Features

As a data warehouse solution,
RedShift has a few features:

* Saves trouble, if you also use other AWS services.
Has built-in monitoring, can also combine with AWS CloudWatch if customization needed;
the `COPY` command recommended for inserting data is tied to AWS S3;
high availability, extensibility, backup are all guaranteed by AWS.

* Provides a full suite of `PostgreSQL` syntax.
Basically anywhere compatible with `PostgreSQL`, swap the `DBDriver` and you can use it painlessly.
But RedShift only provides a SQL standard,
if you need to do non-SQL data storage (like files),
it'll be very strained. ~~by design. wontfix~~

* Expensive, relatively speaking.
The cheapest instance type (dc1.large, 15GB Mem, 0.16TB SSD) is pricing roughly over ten thousand yuan per year,
not counting labor cost, definitely more expensive than building your own data warehouse.
But if you count labor cost... another matter.


### Deployment

The main steps to deploy and use RedShift are as follows:

1. Don't rush to create an instance, first walk through the AWS tutorial,
you'll get an initial understanding of COPY/Encoding/Cluster.
~~For classmates who don't like reading English docs, you can switch to Chinese in the upper right~~

2. Create an appropriate AWS RedShift instance.
Congratulations on completing the achievement _build a data warehouse from scratch_.

3. Connect with business, e.g., choose appropriate Driver.
We use django, can directly use `psycopg2` to connect.
Then there's general business operations like ETL, caching, charts, etc.


### Lessons

After using RedShift for a while,
some things I learned:

* **SQL statements aren't directly executed, but compiled then dispatched for execution**.

No matter what statement we execute, even a single `INSERT INTO` operation,
RedShift compiles before executing, taking 500ms minimum _so use COPY to do data import_.
For another example we deployed four RedShift nodes, then after
`SELECT * FROM orders WHERE business_id = 100` finishes compiling,
RedShift will dispatch the command to each node based on the partition key `DISTKEY` chosen at table creation.
So reasonable table structure is also key to query speed _the generic ~~nonsense~~ truth_.


* **Use COPY command to insert data; for updates, COPY to a temp table, then use DELETE USING + INSERT INTO to update data**

Because each SQL has to be compiled, do batch operations as much as possible, single-row operations are very stupid.
(Just like how stupid we were at first =\_=)
RedShift COPY command supports GZIP, JSON, From S3 and various other operations,
in most cases, loading speed and storage efficiency are both better than ordinary INSERT.
Similarly, updating a single row uses the delete-then-add approach.


* **Periodic Data Warehouse Maintenance**

RedShift doesn't auto-recycle the space released by DELETE/UPDATE,
need users to manually run the `VACUUM` command to clean tables.
`VACUUM` itself is an IO-intensive operation,
so best to run it on a schedule during idle time (e.g., 4 AM).


* **Mind the Table Constraints**

In RedShift,
`unique / primary key / foreign key` are all informational,
no actual constraint power.

Also RedShift.varchar stores single-byte characters,
like MySQL's `utf8` defaults to three-byte characters,
if you use `utf8mb4` it's four-byte characters.
So MySQL's varchar(50) converted to RedShift should be varchar(200).
_Left by those who got bitten by Emoji_


## Summary

In summary,
RedShift's biggest advantage lies in trading money for productivity,
simple to use, is AWS family-bucket users' solution for data warehouse.
Specific usage with extra care, nothing particularly special.

But recently it seems we paid Amazon quite a bit of money,
they sent engineers to the door for free support.

Little Xie thought.


## Extracurricular Reading

* [AWS - RedShift Official Tutorial - https://docs.aws.amazon.com/zh_cn/redshift/latest/dg/tutorial-tuning-tables.html][aws-redshift]

* [CoolShell - Talking about website performance tech via 12306.CN - https://coolshell.cn/articles/6470.html][coolshell-12306]

* [Wikipedia - Data Warehouse - https://en.wikipedia.org/wiki/Data_warehouse][wiki-dw]

* [Fully understanding the difference between utf8 and utf8mb4 in mysql - https://my.oschina.net/xsh1208/blog/1052781][utf8mb4]

* [Xiqiao - Historical Tragedy - https://blog.xiqiao.info/2013/01/14/1366][utf8-enough]


[cash-cow]: /what-is-cash-cow-en
[aws-redshift]: https://docs.aws.amazon.com/zh_cn/redshift/latest/dg/tutorial-tuning-tables.html
[coolshell-12306]: https://coolshell.cn/articles/6470.html
[wiki-dw]: https://en.wikipedia.org/wiki/Data_warehouse
[utf8mb4]: https://my.oschina.net/xsh1208/blog/1052781
[utf8-enough]: https://blog.xiqiao.info/2013/01/14/1366
