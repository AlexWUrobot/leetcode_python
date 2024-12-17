/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>
#include <queue> // For BFS in RoutingService
#include <unordered_set>
#include <algorithm> // Include this header for std::reverse

// Class responsible for managing the city map
class CityMap {
 public:
  // Constructor to initialize the city map
  CityMap(const std::vector<std::vector<int>>& map) : cityMap_(map) {}

  // Function to add a new location (node) to the map
  void addLocation() {
    int newSize = cityMap_.size() + 1;
    for (auto& row : cityMap_) {
      row.push_back(0); // Add 0 (no path) to existing rows
    }
    cityMap_.push_back(std::vector<int>(newSize, 0)); // Add new row
  }

  // Function to add a new path (edge) between two locations
  void addPath(int location1, int location2) {
    if (isValidLocation(location1) && isValidLocation(location2)) {
      cityMap_[location1][location2] = 1;
      cityMap_[location2][location1] = 1; // Bidirectional path
    }
  }

  // Function to check if a move between two locations is valid
  bool isPath(int from, int to) const {
    return isValidLocation(from) && isValidLocation(to) && cityMap_[from][to] == 1;
  }

  // Function to get the number of locations in the city
  int size() const { return cityMap_.size(); }

  // Function to get the entire city map
  const std::vector<std::vector<int>>& getMap() const { return cityMap_; }

 private:
  std::vector<std::vector<int>> cityMap_;

  // Helper function to validate a location index
  bool isValidLocation(int location) const {
    return location >= 0 && location < cityMap_.size();
  }
};

// Class responsible for routing and finding the shortest path
class RoutingService {
 public:
  // Constructor accepting a CityMap reference
  RoutingService(const CityMap& cityMap) : cityMap_(cityMap) {}

  // Function to find the shortest path using BFS
  std::vector<int> findShortestPath(int start, int target) {
    std::vector<int> previous(cityMap_.size(), -1); // Tracks the previous node
    std::queue<int> queue;                         // BFS queue
    std::unordered_set<int> visited;               // Set to track visited nodes

    queue.push(start);    // Start BFS from the starting location
    visited.insert(start);

    // BFS loop to explore nodes
    while (!queue.empty()) {
      int current = queue.front();
      queue.pop();

      // If the target is reached, reconstruct the path
      if (current == target) {
        return reconstructPath(previous, start, target);
      }

      // Explore neighbors
      for (int neighbor = 0; neighbor < cityMap_.size(); ++neighbor) {
        if (cityMap_.isPath(current, neighbor) && visited.find(neighbor) == visited.end()) {
          queue.push(neighbor);
          visited.insert(neighbor);
          previous[neighbor] = current; // Record the path
        }
      }
    }

    // Return an empty path if target is unreachable
    return {};
  }

 private:
  const CityMap& cityMap_;

  // Helper function to reconstruct the path from 'previous' vector
  std::vector<int> reconstructPath(const std::vector<int>& previous, int start, int target) {
    std::vector<int> path;
    for (int at = target; at != -1; at = previous[at]) {
      path.push_back(at);
    }
    std::reverse(path.begin(), path.end());
    if (path.front() == start) {
      return path;
    }
    return {}; // Return empty if no path found
  }
};

// Class representing the Delivery Robot
class DeliveryRobot {
 public:
  // Constructor with dependency injection of CityMap and RoutingService
  DeliveryRobot(const CityMap& cityMap, RoutingService& routingService, int startLocation)
      : cityMap_(cityMap), routingService_(routingService), currentLocation_(startLocation) {}

  // Function to move the robot to a specific destination
  void move(int destination) {
    if (cityMap_.isPath(currentLocation_, destination)) {
      std::cout << "Moving from " << currentLocation_ << " to " << destination << ".\n";
      currentLocation_ = destination;
    } else {
      std::cout << "Invalid move from " << currentLocation_ << " to " << destination << ".\n";
    }
  }

  // Function to find and print the shortest path to the target location
  void findAndFollowShortestPath(int target) {
    std::vector<int> path = routingService_.findShortestPath(currentLocation_, target);
    if (path.empty()) {
      std::cout << "No path found to " << target << ".\n";
    } else {
      std::cout << "Shortest Path: ";
      for (int location : path) {
        std::cout << location << " ";
      }
      std::cout << "\n";

      // Simulate moving along the path
      for (size_t i = 1; i < path.size(); ++i) {
        move(path[i]);
      }
    }
  }
  // Getter function to access the current location
  int getCurrentLocation() const {
    return currentLocation_;
  }
 private:
  const CityMap& cityMap_;
  RoutingService& routingService_;
  int currentLocation_;
};

// Main function to demonstrate the functionality
int main() {
  // Define the city map as an adjacency matrix
  std::vector<std::vector<int>> cityMapData = {
      {0, 1, 1, 0, 0},
      {1, 0, 1, 1, 0},
      {1, 1, 0, 1, 1},
      {0, 1, 1, 0, 1},
      {0, 0, 1, 1, 0},
  };

  // Create CityMap and RoutingService instances
  CityMap cityMap(cityMapData);
  RoutingService routingService(cityMap);

  // Create a DeliveryRobot at location 0
  DeliveryRobot robot(cityMap, routingService, 0);

  // Demonstrate robot movements and shortest path finding
  robot.move(2);
  robot.move(4);
  robot.move(1);

  std::cout << "Current Position (Start): "<<robot.getCurrentLocation() << "\n";
  std::cout << "Finding shortest path from current location to 4:\n";
  robot.findAndFollowShortestPath(1);

  // Add a new location and path dynamically
  cityMap.addLocation();
  cityMap.addPath(4, 5);

  std::cout << "Current Position (Start): "<<robot.getCurrentLocation() << "\n";
  std::cout << "Finding shortest path to new location 5:\n";
  robot.findAndFollowShortestPath(5);

  return 0;
}
