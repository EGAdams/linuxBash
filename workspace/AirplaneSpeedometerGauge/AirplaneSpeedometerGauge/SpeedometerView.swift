import UIKit

class SpeedometerView: UIView {
    private var rimImageView: UIImageView!
    private var faceImageView: UIImageView!
    private var ticksImageView: UIImageView!
    private var speedLabel: UILabel!
    
    func setSpeed(_ speed: Int) {
        speedLabel.text = "\(speed) km/h"
    }
    
    func setRimImage(_ image: UIImage) {
        rimImageView.image = image
    }
    
    func setFaceImage(_ image: UIImage) {
        faceImageView.image = image
    }
    
    func setTicksImage(_ image: UIImage) {
        ticksImageView.image = image
    }
}
