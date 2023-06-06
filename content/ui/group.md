Using `chainctl`, you can check for the ID of your group.

```sh
chainctl iam groups ls -o table
```

You'll receive output in the form of a table with information about your current groups, similar to the following.

```
                     ID                    |       NAME       | DESCRIPTION
-------------------------------------------+------------------+--------------

  b9adda06841c1d34dfa73d5902ed44b5448b7958 | enforce-demo-group |
```

> **Note**: If you don't receive output like the above at all, you can create a new group by running `chainctl iam groups create --no-parent` to create a new group. The `--no-parent` flag will ensure that the new group will be a new root group; this means it won't have any connections to your existing Chainguard resources, making it safe for experimentation. After group creation, you can run `chainctl iam groups ls -o table` again to retrieve the new group's ID.

Next, create a variable that stores the ID in the left column for later steps in this tutorial. In the following command, replace `$GROUP_ID` with the relevant ID.

```sh
export GROUP=$GROUP_ID
```

In the UI, you can also check for groups to which you belong from the filter modal, which you can open by using the group selector on the left navigation menu.

![Group dropdown](/images/group-dropdown.png)

You can check here to see the groups to which you belong and filter resources based on group ownership.
