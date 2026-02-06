param_from = {"from_"}
param_target = {"target_id"}
param_name = {"faction_name"}
param_stat = {"stat_key", "stat_keys"}
param_log = {"attack_log_id", "log_id"}
param_ids = {"category_ids", "honor_ids", "item_ids", "medals_ids", "territory_ids"}
param_filters = {"attack_filters", "crimes_filter", "property_filters"}
param_id = {
    "chain_id",
    "crime_id",
    "faction_id",
    "item_id",
    "listing_id",
    "log_category_id_torn",
    "property_id",
    "property_type_id",
    "race_id",
    "raid_war_id",
    "ranked_war_id",
    "team_id",
    "territory_war_id",
    "thread_id",
    "track_id",
    "user_id",
}
param_cat = {
    "balance_category",
    "bazaar_category",
    "car_category",
    "contributors_category",
    "crimes_category",
    "item_category",
    "leaderboard_category",
    "list_category",
    "log_category_id",
    "news_category",
    "race_category",
    "report_category",
    "stat_category",
    "warfare_category",
}
param_group = {
    "from": param_from,
    "target": param_target,
    "name": param_name,
    "stat": param_stat,
    "log": param_log,
    "ids": param_ids,
    "filters": param_filters,
    "id": param_id,
    "cat": param_cat,
}
parameter_map = {key: group for group, keys in param_group.items() for key in keys}