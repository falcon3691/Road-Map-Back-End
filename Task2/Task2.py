import socket
import requests
import json
from collections import defaultdict

def getEvent(username):
    try:
        url = f"https://api.github.com/users/{username}/events"
        response = requests.get(url)

        if response.status_code == 200:
            events = response.json()  # JSON formatına dönüştür
            
            # Eventleri türlerine göre gruplandır
            grouped_events = defaultdict(list)
            for event in events:
                event_type = event.get("type", "Unknown")
                grouped_events[event_type].append(event)

            # Konsola okunabilir formatta yazdır
            for event_type, event_list in grouped_events.items():
                print(f"🟢 Event Type: {event_type} - Count: {len(event_list)}")
                
                for event in event_list:
                    event_id = event.get("id", "N/A")
                    actor = event.get("actor", {}).get("login", "Unknown")
                    repo = event.get("repo", {}).get("name", "Unknown Repo")
                    created_at = event.get("created_at", "Unknown Time")
                    
                    details = f"  - ID: {event_id} | Repo: {repo} | Time: {created_at} | By: {actor}"
                    
                    # PushEvent için commit mesajlarını alalım
                    if event_type == "PushEvent":
                        commits = event.get("payload", {}).get("commits", [])
                        commit_messages = [commit.get("message", "No message") for commit in commits]
                        details += f"\n    ↳ Commits: {', '.join(commit_messages[:2])}"  # İlk 2 commit mesajını göster
                    
                    # CreateEvent için referans türünü alalım
                    if event_type == "CreateEvent":
                        ref_type = event.get("payload", {}).get("ref_type", "Unknown")
                        ref = event.get("payload", {}).get("ref", "N/A")
                        details += f" | Created: {ref_type} - {ref}"
                    
                    # ForkEvent için fork edilen repo bilgisi
                    if event_type == "ForkEvent":
                        forked_repo = event.get("payload", {}).get("forkee", {}).get("full_name", "Unknown Repo")
                        details += f" | Forked: {forked_repo}"
                    
                    # IssuesEvent için issue bilgisi
                    if event_type == "IssuesEvent":
                        action = event.get("payload", {}).get("action", "Unknown")
                        issue_title = event.get("payload", {}).get("issue", {}).get("title", "No Title")
                        details += f" | Issue: {action} - {issue_title}"
                    
                    # IssueCommentEvent için yorum bilgisi
                    if event_type == "IssueCommentEvent":
                        comment = event.get("payload", {}).get("comment", {}).get("body", "No Comment")
                        details += f" | Comment: {comment[:50]}..."
                    
                    # PullRequestEvent için PR bilgisi
                    if event_type == "PullRequestEvent":
                        action = event.get("payload", {}).get("action", "Unknown")
                        pr_title = event.get("payload", {}).get("pull_request", {}).get("title", "No Title")
                        details += f" | PR: {action} - {pr_title}"
                    
                    # WatchEvent (Star verilmişse)
                    if event_type == "WatchEvent":
                        details += " | Starred the repository"
                    
                    print(details)
                print("-" * 50)
        
        elif response.status_code == 404:
            print(f"⚠️  Page not found! Error code: {response.status_code}")
        else:
            print(f"⚠️  Request failed! HTTP Status: {response.status_code}")
    
    except requests.exceptions.ConnectionError:
        print("⚠️  Connection error! Please check your internet connection.")
    except socket.gaierror:
        print("⚠️  DNS resolution error! Unable to resolve 'api.github.com'.")
    except requests.exceptions.Timeout:
        print("⏳  Request timed out. Please try again later.")
    except requests.exceptions.HTTPError as e:
        print(f"❌  HTTP Error! Status code: {e.response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️  Unexpected error occurred: {e}")

username = input("Please enter the username: ")
getEvent(username)
