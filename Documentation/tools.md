```
I feel #{good~swell~amazing} today my dear chap
```

**Random Substitution** - anything in #{} separated by ~(or , if no tilde were found) will be randomly picked and put in the lists place.

Returns: **I feel good today my dear chap**

---------------

```
Tau is m{PI * 2}
```

**Math Blocks** - Anything in m{} will be treated as a mathematical expression and replaced

Returns: **Tau is 6.283185307179586**

---------------

```
!{user=#{Yenni~Carl~PySnow~Kintark}}
$user is looking great today.
```

**Variable assignment and Usage** - **!{} has to be on its own line** and it assigns a value to a name allowing you to reuse it through
the tag.

Returns: **Carl is looking great today**

---------------

```
You look ?{delightfully} awful
```

**Optional blocks** - anything in ?{} has a 50% chance to not be added in at all.

Returns: **You look awful**

---------------

```
Its currently the year strf{%Y}
```

**Date Formatting** - Formats the date and replaces %y with year, %m with month and %d with day.

Returns: **Its currently the year 2018**