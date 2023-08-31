import UIKit
import Alamofire
import SwiftyJSON

class NetworkHelper {
    static func sendRequest(url: URL, parameters: [String: Any], completion: @escaping (Data?, Error?) -> Void) {
        Alamofire.request(url, method: .post, parameters: parameters, encoding: JSONEncoding.default)
            .validate()
            .responseData { response in
                switch response.result {
                case .success(let data):
                    completion(data, nil)
                case .failure(let error):
                    completion(nil, error)
                }
            }
    }
    
    static func parseResponse(data: Data) -> [String: Any] {
        do {
            let json = try JSON(data: data)
            return json.dictionaryObject ?? [:]
        } catch {
            print("Failed to parse response: \(error)")
            return [:]
        }
    }
}
