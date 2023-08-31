import UIKit

class AnimationHelper {
    static func animateSpeedometerView(speedometerView: SpeedometerView, metrics: SpeedometerMetrics) {
        UIView.animate(withDuration: 0.5) {
            speedometerView.setSpeed(metrics.speed)
            // Animate other properties of the speedometer view based on the metrics
        }
    }
}
