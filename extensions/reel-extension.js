module.exports = function () {
  this.blockMacro('reel', function () {
    const self = this

    self.process(function (parent, target, attrs) {
      const imageUrl = attrs.image
      const placeholderImage = 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImdyYWQiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPjxzdG9wIG9mZnNldD0iMCUiIHN0eWxlPSJzdG9wLWNvbG9yOiM2NjdlZWE7c3RvcC1vcGFjaXR5OjEiLz48c3RvcCBvZmZzZXQ9IjEwMCUiIHN0eWxlPSJzdG9wLWNvbG9yOiM3NjRiYTI7c3RvcC1vcGFjaXR5OjEiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48cmVjdCB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCIgZmlsbD0idXJsKCNncmFkKSIvPjx0ZXh0IHg9IjUwJSIgeT0iNDAlIiBmb250LXNpemU9IjQ4IiBmaWxsPSIjRkZGIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkeT0iLjNlbSI+4oCTPC90ZXh0Pjx0ZXh0IHg9IjUwJSIgeT0iNTAlIiBmb250LXNpemU9IjE4IiBmaWxsPSIjRkZGIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkeT0iLjNlbSI+SW5zdGFncmFtIFJlZWw8L3RleHQ+PHRleHQgeD0iNTAlIiB5PSI2MCUiIGZvbnQtc2l6ZT0iMTQiIGZpbGw9IiNGRkYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGR5PSIuM2VtIiBvcGFjaXR5PSIwLjgiPkNsaWNrIHRvIHdhdGNoPC90ZXh0Pjwvc3ZnPg=='

      const imageHtml = imageUrl ? `<img src="${imageUrl}" alt="Instagram Reel" style="width: 100%; display: block; height: auto;" onerror="this.style.display='none'; this.parentElement.style.background='url(\\'${placeholderImage}\\')'; this.parentElement.style.backgroundSize='cover';"/>` : `<div style="width: 100%; height: 100%; background: url('${placeholderImage}'); background-size: cover; background-position: center;"></div>`

      return self.createBlock(parent, 'pass', `
<div style="margin: 20px 0;">
  <a href="https://www.instagram.com/reels/${target}/" target="_blank" style="text-decoration: none; border: none;">
    <div style="position: relative; width: 400px; height: 300px; border-radius: 12px; overflow: hidden; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.15); display: inline-block;">
      ${imageHtml}
      <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 40px; color: white; background: rgba(0,0,0,0.6); border-radius: 50%; padding: 10px 15px; pointer-events: none; transition: all 0.3s ease;">▶</div>
    </div>
  </a>
</div>
      `)
    })
  })
}
