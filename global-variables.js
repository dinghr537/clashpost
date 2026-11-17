/**
 * hasNotification {Boolean} 是否发布通知，如果填 false 则视为不发布，前端不再运行通知相关的代码，可节省性能。
 * notificationCount {Number} 通知角标显示的数字，默认为 1，只有当同时发布多条通知时才需要修改这个值。
 * currentNotificationId {Number} 当前通知的 ID，前端需要用这个值区分接收到的是全新通知还是以前发布过的通知。发布新通知时请将这个值 +1
 * notificationHTML {String} 通知内容，可使用 HTML 代码。如果发布多条通知，通常使用 <hr> 标签分割。
 */
export const notificationInfo = {
    "hasNotification": true,
    "notificationCount": 1,
    "currentNotificationId": 19,
    "notificationTitle": "升级数据更新至 19 本（2026-11-16 版本）",
    "notificationHTML": "<p>本项目作为部落驿站的继承项目，专注于升级等级、费用、时间与前置条件查询。</p>" +
        "<p>已收录 19 本更新：19 级大本营、12 种小队与小队训练营、尖刺塔、烟花炮手塔、英勇法术、守卫神殿，以及各单位的新等级和旧等级降价。出了新等级的建筑已按官方公告移除超级充能。</p>" +
        "<p>数值依次参考 Supercell 官方公告、Clash of Clans Wiki 和 ClashKing 整理的游戏数据，各页底部注明来源。新等级暂缺的数据显示为“待更新”；可能已调整、但暂时只有旧数值的以 * 标出。</p>" +
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
