# Carlbot specific variables!

You can count on these variables to be available in any tag that you make with
carl bot. The feature set may be limited when it comes to editing Embeds!


`{user}` and `{target}` these point to; the person using the tag, and the
first person they mention, respectively. If using `{target}` and there is no
mention then it will default to the person using the tag. There are cool parameters
you can use when accessing these variables such as:

(Remember, anything that works with `{user}` will work with `{target}`)

- `{user(id)}` returns the unique discord user ID, eg `235148962103951360`
- `{user(proper)}` returns a full/proper 'username#disc' string, eg `Carl-bot#1536`
- `{user(mention)}` depending on your server, returns an actual ping to the person,
eg `@carlbot`
- `{user(avatar)}` returns a url that points directly to the users avatar, eg 
`https://cdn.discordapp.com/avatars/235148962103951360/cececd50fdc87b29929e65c768f24ad6.png?size=1024`

