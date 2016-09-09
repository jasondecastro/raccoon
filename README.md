# Raccoon

People still write SQL every single day. I'm almost positive that not everyone uses Active Record or SQLAlchemy and other ORMs. 

It's a pretty established fact that SQL is so tedious to code. It's not that it's hard necessarily, it's just really annoying to write.

Introducing **Raccoon**.

Raccoon is a library and DSL built in Python that acts as both a language wrapper to SQL and a migrater at the same time. Here is how it works:

```
flatironschool:
  students:
    first_name
    last_name
    
  instructors:
    first_name
    last_name
```

This is pretty self-explanatory. `flatironschool` is the database name, `students` and `instructors` are the table names, and what goes within them are the columns.

How would you write such a model in SQL?

```
USE `flatironschool`;

CREATE TABLE IF NOT EXISTS `students` (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name STRING,
  last_name STRING
);

CREATE TABLE IF NOT EXISTS `instructors` (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name STRING,
  last_name STRING
);
```

Want to know something cool? The first Raccoon example means exactly the same as the second SQL example. Raccoon is an abstraction of all of that extra syntax you would typically have to write in SQL.

# Reactions

This might make me sound like a hypocrite, because I'm always advocating for explicity over implicity, but can we make an exception for SQL? Reactions are basically an alias for implicit responses that Raccon is smart enough to interpret for you.

Every column that you create in Raccoon reacts as a `STRING` datatype, since I assume that's the most popular. 

Also, creating the `id` is abstracted for you as well. Each table will have an `id` column that acts both as a `PRIMARY KEY` and autoincrements.

# Smart

There are a few keywords that Raccoon automatically reacts too. For example, if you named a column with a question mark after the name, like:

```
flatironschool:
  students:
    admin?
```

It will implicitly set that column as a boolean and remove the question mark from the name. If you type in `password`, it will rename it to `password_digest`. There are bunch of cool and handy keywords that Raccoon reacts to, almost accurately.

# Modular

Well, what if you don't want to be implicit? That's fine too, you can add your own custom properties if you'd like.

```
flatironschool:
  students:
    pass_code integer 
    grade string
```

This will remove the implicit `STRING` and replace it for the attributes you give it after the column name.

# Migrations

You have two options when running a Raccoon schema file. 

```
raccoon schema.cc
```

The basic command above will take your schema and convert it to SQL, but it will also find your database and run the converted SQL.

```
raccoon schema.cc raw
```

This command is much like the first one, except it wont run the converted SQL for you. Instead, a file will be created called schema.sql with the converted SQL inside of it, for you to do as you please with it.

# Versatile

There are tens, possibly even hundreds, of different database engines. You might be thinking how Raccoon works for all of them, despite the small syntatical changes between them.

Raccoon at the time supports 3 database engines, and those include the following:

```
SQLite
MySQL
PostgreSQL
```

By default, Raccoon will compile the schema and run it as SQLite, unless explicitly told not to. Which leads me to the next section.

# Modular

You can customize how Raccoon reacts to certain things. I advocate for explicit over implicit all of the time, why would I not give you the option to be explicit?

```
engine: postgres
user: root
pass: letmein

flatironschool:
  students:
    first_name
    last_name
```

That will react to Postgres instead of the default SQLite.

```
engine: postgres
user: root
pass: letmein

reactions: no

flatironschool:
  students:
    first_name string
    last_name string
```

That is the power of **Raccoon**.

# Conclusion

Raccoon will publicly release as version one in a couple of weeks, and it will be open-source. This is a really simple and straightforward approach to writing SQL and I would recommend everyone to use it, or at least give it a shot.

Say yes to Raccoon, say no more to SQL.

*(If you would like to check out version 0.5 right now, it's [on my GitHub](https://github.com/jasondecastro/raccoon))*
