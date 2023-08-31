import UIKit
import CoreData

class DataStorageManager {
    private let context: NSManagedObjectContext
    
    init() {
        guard let appDelegate = UIApplication.shared.delegate as? AppDelegate else {
            fatalError("Unable to access AppDelegate")
        }
        context = appDelegate.persistentContainer.viewContext
    }
    
    func saveMetrics(_ metrics: SpeedometerMetrics) {
        let entity = NSEntityDescription.entity(forEntityName: "Metrics", in: context)!
        let metricsObject = NSManagedObject(entity: entity, insertInto: context)
        
        metricsObject.setValue(metrics.speed, forKey: "speed")
        metricsObject.setValue(metrics.yaw, forKey: "yaw")
        metricsObject.setValue(metrics.otherMetrics, forKey: "otherMetrics")
        
        do {
            try context.save()
        } catch {
            print("Failed to save metrics: \(error)")
        }
    }
    
    func retrieveMetrics() -> SpeedometerMetrics {
        let fetchRequest = NSFetchRequest<NSFetchRequestResult>(entityName: "Metrics")
        
        do {
            let result = try context.fetch(fetchRequest)
            if let metricsObject = result.first as? NSManagedObject {
                let speed = metricsObject.value(forKey: "speed") as? Int ?? 0
                let yaw = metricsObject.value(forKey: "yaw") as? Int ?? 0
                let otherMetrics = metricsObject.value(forKey: "otherMetrics") as? Int ?? 0
                
                return SpeedometerMetrics(speed: speed, yaw: yaw, otherMetrics: otherMetrics)
            }
        } catch {
            print("Failed to retrieve metrics: \(error)")
        }
        
        return SpeedometerMetrics(speed: 0, yaw: 0, otherMetrics: 0)
    }
}
