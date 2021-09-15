import pandas as pd
import os

def activity_ratio_per_customer(activity_df,activities,target_customers):
    '''
    Params:
        activity_df     : activity.csv dataset in pandas dataframe
        activities      : list of all activity types
        target_customers: list of customers who closed the deals
    
    Returns:
        activity_dict   : a dictonary where customer ids are keys and
                        another dictionary is assigned to each key where
                        activity types are keys and ratios are values
                        
                        Example:

                        {
                            "customer_id":
                            {
                                "activity_type" : ratio
                            }
                        }
    '''

    activity_dict = { customer : { activity : 0 for activity in activities } for customer in target_customers }
    for key in activity_dict.keys(): activity_dict[key]['total_act'] = 0

    for _ , row in activity_df.iterrows():
        if row['customer'] in activity_dict.keys():
            activity_dict[row['customer']][row['activity_type']] += row['activity_count']
            activity_dict[row['customer']]['total_act'] += row['activity_count']

    for customer_key, value_dict in activity_dict.items():
        total_activities = activity_dict[customer_key]['total_act']
        if total_activities :
            for activity_key, value in value_dict.items():
                activity_dict[customer_key][activity_key] = value / total_activities

    return activity_dict

def contribution_value_per_activity(activity_dict,activities):
    '''
    Params:
        activity_dict   : a dictonary containing contribution ratios per customer
        activities      : list of all activity types
    
    Returns:
        contribution_list   : each element in the list contains a dictionary
                            {'activity_type': activity type, 'contribution': contribution value} 
    '''

    contribution_list = []

    for activity in activities:
        contribution = 0.0
        for customer in activity_dict.keys():
            contribution += activity_dict[customer][activity]
            
        contribution /= len(activity_dict)
        contribution_list.append({'activity_type':activity, 'contribution':contribution})

    return contribution_list

def main():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(cur_dir,"data")

    activity_df = pd.read_csv(data_dir+"\\activity.csv")
    target_df = pd.read_csv(data_dir+"\\target.csv")

    activities = list(set(activity_df['activity_type']))
    target_customers = target_df['customer'].to_list()

    print("Calculating activity ratio per customer....")
    activity_dict = activity_ratio_per_customer(activity_df,activities,target_customers)

    print("Assigning contribution value per activity....")
    contribution_list = contribution_value_per_activity(activity_dict,activities)

    print("Saving activity_contribution.csv")
    activity_contribution_df = pd.DataFrame(data=contribution_list,columns=['activity_type','contribution'])
    activity_contribution_df.to_csv(cur_dir+"\\activity_contribution.csv",index=False)

    print(f"Head to => {cur_dir}\\activity_contribution.csv to find the saved CSV file")

    return

if __name__ == "__main__":
    main()
