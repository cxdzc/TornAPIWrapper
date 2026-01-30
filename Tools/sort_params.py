param_from = {"from_"}
param_target = {"target_id"}
param_name = {"faction_name"}
param_stat = {"stat_key", "stat_keys"}
param_log = {"attack_log_id", "log_id"}
param_ids = {"honor_ids", "item_ids", "medals_ids", "territory_ids"}
param_filters = {"attack_filters", "crimes_filter", "property_filters"}
param_id = {"category_id", "chain_id", "crime_id", "faction_id", "item_id", "listing_id", "log_category_id_torn", "property_id", "property_type_id", "race_id", "raid_war_id", "ranked_war_id", "team_id", "territory_war_id", "thread_id", "track_id", "user_id"}
param_cat = {"balance_category", "bazaar_category", "car_category", "contributors_category", "crimes_category", "item_category", "leaderboard_category", "list_category", "log_category_id", "news_category", "race_category", "report_category", "stat_category", "warfare_category"}

params = {
    "param_from": param_from,
    "param_target": param_target,
    "param_name": param_name,
    "param_stat": param_stat,
    "param_log": param_log,
    "param_ids": param_ids,
    "param_filters": param_filters,
    "param_id": param_id,
    "param_cat": param_cat,
}

for name, values in params.items():
    sorted_items = ", ".join(f'"{v}"' for v in sorted(values))
    print(f'{name} = {{{sorted_items}}}')