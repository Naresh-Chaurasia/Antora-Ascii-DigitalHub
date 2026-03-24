module.exports = function () {
  this.blockMacro('reel', function () {
    const self = this

    self.process(function (parent, target, attrs) {
      const image = attrs.image || '/_images/default-reel.png'

      return self.createBlock(parent, 'pass', `
        <div class="reel-container">
          <a href="https://www.instagram.com/reels/${target}/" target="_blank">
            <div class="reel-card">
              <img src="${image}" class="reel-thumbnail"/>
              <div class="play-button">▶</div>
            </div>
          </a>
        </div>
      `)
    })
  })
}
