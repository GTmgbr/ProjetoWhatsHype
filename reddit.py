import redditwarp.SYNC

client = redditwarp.SYNC.Client()

it = client.p.front.pull.hot(37)
l = list(it)
for subm in l:
    print("r/{0.subreddit.name} | {0.id36}+ ^{0.score} | {0.title!r:.80}".format(subm))
    print(dir(subm))

#['apply_removal_reason', 'approve', 'archived', 'author', 'author_display_name', 'b', 'client', 'comment_count', 'created_at', 'created_ut', 'd', 'delete', 'distinguish', 'distinguished', 'edited', 'edited_at', 'edited_ut', 'event', 'flair', 'id', 'id36', 'idn', 'in_contest_mode', 'is_crosspostable', 'is_edited', 'is_poster_profile_pinned', 'is_robot_indexable', 'link', 'lock', 'locked', 'me', 'mod', 'nsfw', 'num_crossposts', 'oc', 'permalink', 'permalink_path', 'removal_category', 'remove', 'reply', 'reports', 'score', 'score_hidden', 'send_removal_comment', 'send_removal_message', 'spoiler', 'stickied', 'sticky', 'subreddit', 'suggested_sort', 'title', 'undistinguish', 'unlock', 'unsticky', 'upvote_ratio']

# # How many subscribers does r/Python have?
# subr = client.p.subreddit.fetch_by_name('Python')
# print(subr.subscriber_count)
#
# # Display the top submission of the week in the r/YouShouldKnow subreddit.
# m = next(client.p.subreddit.pull.top('YouShouldKnow', amount=1, time='week'))
# print(f'''\
# {m.permalink}
# {m.id36}+ ^{m.score} | {m.title}
# Submitted {m.created_at.astimezone().ctime()}{' *' if m.is_edited else ''} \
# by u/{m.author_display_name} to r/{m.subreddit.name}
# ''')
#
# Get the first comment of a submission.
tree_node = client.p.comment_tree.fetch('uc8i1g', sort='top', limit=1)
c = tree_node.children[0].value
print(f'''\
{c.submission.id36}+{c.id36} ^{c.score}
u/{c.author_display_name} says:
{c.body}
''')