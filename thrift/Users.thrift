struct Image {
  1:string URL,
  2:i32 size
}

typedef i64 TUSerId

enum UserType { ADMIN=1,USER=2 }

struct User {
  1:TUSerId id,
  2:string name,
  3:string password,
  4:Image icon
}

service UserAuthenticator {
  void ping(),
  User authenticateUser(1:string name, 2:string password),
  Image getUserIcon(1:TUSerId userId),
  bool isValidUser(1:TUSerId userId),
  oneway void logoutUser(1:i64 userId)
}
