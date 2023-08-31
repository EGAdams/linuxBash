import Foundation

class UserDefaultsHelper {
    static func saveObject(object: Any, forKey: String) {
        UserDefaults.standard.set(object, forKey: forKey)
    }
    
    static func retrieveObject(forKey: String) -> Any? {
        return UserDefaults.standard.object(forKey: forKey)
    }
}
