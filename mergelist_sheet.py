import pandas as pd

def merge_lists_with_names(lists, names):
    merged_dfs = []
    for lst, name in zip(lists, names):
        df = pd.DataFrame(lst)
        df.columns = [f"{name}_{col}" for col in df.columns]
        merged_dfs.append(df)
    merged_df = pd.concat(merged_dfs, axis=1)
    return merged_df

# Example lists of lists
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
list3 = [['apple', 'banana', 'orange'], ['grape', 'kiwi', 'pear'], ['watermelon', 'pineapple', 'mango']]

# Example names for each list
names = ['Numbers', 'Alphabets', 'Fruits']

# Merge the lists with names
merged_data = merge_lists_with_names([list1, list2, list3], names)

# Write the merged data to an Excel file
merged_data.to_excel("output.xlsx", index=False)

print("Merged data written to output.xlsx")


###########################

import pandas as pd

def combine_lists_to_dataframe(lists, headings):
    # Create a DataFrame for each list of lists
    dfs = [pd.DataFrame(lst, columns=headings[i]) for i, lst in enumerate(lists)]
    
    # Concatenate the DataFrames along rows
    combined_df = pd.concat(dfs, ignore_index=True)
    
    return combined_df

# Example lists of lists
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
list3 = [['apple', 'banana', 'orange'], ['grape', 'kiwi', 'pear'], ['watermelon', 'pineapple', 'mango']]

# Example headings for each list of lists
headings = [['Numbers', 'Numbers', 'Numbers'],
            ['Alphabets', 'Alphabets', 'Alphabets'],
            ['Fruits', 'Fruits', 'Fruits']]

# Combine the lists into one DataFrame
combined_data = combine_lists_to_dataframe([list1, list2, list3], headings)

# Write the combined data to an Excel file
combined_data.to_excel("output.xlsx", index=False)

print("Combined data written to output.xlsx")