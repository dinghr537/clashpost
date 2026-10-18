/**
 * hasNotification {Boolean} 是否发布通知，如果填 false 则视为不发布，前端不再运行通知相关的代码，可节省性能。
 * notificationCount {Number} 通知角标显示的数字，默认为 1，只有当同时发布多条通知时才需要修改这个值。
 * currentNotificationId {Number} 当前通知的 ID，前端需要用这个值区分接收到的是全新通知还是以前发布过的通知。发布新通知时请将这个值 +1
 * notificationHTML {String} 通知内容，可使用 HTML 代码。如果发布多条通知，通常使用 <hr> 标签分割。
 */
export const notificationInfo = {
    "hasNotification": true,
    "notificationCount": 1,
    "currentNotificationId": 18,
    "notificationTitle": "升级数据同步至 2026-10-13",
    "notificationHTML": "<p>本项目作为部落驿站的继承项目，专注于升级等级、费用、时间与前置条件查询。</p>" +
        "<p>常驻单位、精工防御及本次同步的临时单位已采用 Clash of Clans Wiki 当前表格，补充新增单位与 2026 年更新记录。每页可查看同步日期和来源修订。</p>" +
        "<p>未重新核对的往期临时单位仍保留历史数据，并在页面上说明。</p>" +
        "<p>安装包下载入口通往原部落驿站，点击后会先显示跳转说明。</p>"
};

/**
 * 全局升级数据状态，会在进入升级数据页面的时候调用
 * 
 * availableTempUnits 目前可以训练的临时兵种
 * availableCraftedBuildings 目前可以使用的精工防御
 */
export const availableTempUnits = ["0e1d", "0e0b", "0e0c", "0e07", "0e03"];
export const availableCraftedBuildings = ["0909", "090a", "090b"];
export const temporaryAvailability = {
    startsAt: "2026-10-08T08:00:00Z",
    endsAt: "2026-10-25T08:00:00Z",
    sourceUrl: "https://supercell.com/en/games/clashofclans/blog/news/the-portal-panic-medal-event-rifts-its-way-into-clash/"
};
export function isTemporaryAvailable(unitId, now = Date.now()) {
    return availableTempUnits.includes(unitId) && now >= Date.parse(temporaryAvailability.startsAt) && now < Date.parse(temporaryAvailability.endsAt);
}
