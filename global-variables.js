/**
 * hasNotification {Boolean} 是否发布通知，如果填 false 则视为不发布，前端不再运行通知相关的代码，可节省性能。
 * notificationCount {Number} 通知角标显示的数字，默认为 1，只有当同时发布多条通知时才需要修改这个值。
 * currentNotificationId {Number} 当前通知的 ID，前端需要用这个值区分接收到的是全新通知还是以前发布过的通知。发布新通知时请将这个值 +1
 * notificationHTML {String} 通知内容，可使用 HTML 代码。如果发布多条通知，通常使用 <hr> 标签分割。
 */
export const notificationInfo = {
    "hasNotification": true,
    "notificationCount": 1,
    "currentNotificationId": 17,
    "notificationTitle": "部落驿站升级数据维护说明",
    "notificationHTML": "<p>本项目作为部落驿站的继承项目，专注于升级等级、费用、时间与前置条件查询。</p>" +
        "<p>当前沿用原项目历史资料，各单位的收录进度不同，尚未完成最新版本同步。后续更新会记录来源与同步日期。</p>" +
        "<p>本站仅提供升级数据查询，安装包下载已关闭。</p>"
};

/**
 * 全局升级数据状态，会在进入升级数据页面的时候调用
 * 
 * availableTempUnits 目前可以训练的临时兵种
 * availableCraftedBuildings 目前可以使用的精工防御
 */
export const availableTempUnits = [];
export const availableCraftedBuildings = [];
