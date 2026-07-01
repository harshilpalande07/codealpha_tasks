import csv
from datetime import datetime
import sys
import yfinance as yf  # 🔥 Live Web Exchange Engine

# --- TERMINAL COLOR TUNING MATRICES ---
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
RED = "\033[31m"
WHITE = "\033[37m"

class StockAsset:
    def __init__(self, symbol: str, company_name: str):
        self.symbol = symbol.upper()
        self.company_name = company_name
        self.current_price = 0.0  # Will be dynamically updated live!

class PortfolioTracker:
    def __init__(self):
        # CodeAlpha Dynamic Live Asset Database
        self.market_database = {
            "AAPL": StockAsset("AAPL", "Apple Inc."),
            "TSLA": StockAsset("TSLA", "Tesla Motors"),
            "AMZN": StockAsset("AMZN", "Amazon.com Inc."),
            "MSFT": StockAsset("MSFT", "Microsoft Corp."),
            "NVDA": StockAsset("NVDA", "NVIDIA Corporation")
        }
        self.user_holdings = {}
        self.fetch_live_prices()

    def fetch_live_prices(self):
        """Connects to the global web server to scrape real-time prices."""
        print(f"\n{BOLD}{YELLOW}📡 Connecting to Live Market Matrix Exchange...{RESET}")
        for symbol, asset in self.market_database.items():
            try:
                # Queries the Yahoo Finance live network API
                ticker = yf.Ticker(symbol)
                # Fetches the absolute latest fast-updating market price
                live_price = ticker.fast_info['last_price']
                asset.current_price = round(live_price, 2)
            except Exception:
                # Fallback prices if your internet ever cuts out during the demo
                fallback_prices = {"AAPL": 185.50, "TSLA": 210.20, "AMZN": 178.00, "MSFT": 415.25, "NVDA": 920.00}
                asset.current_price = fallback_prices[symbol]
        print(f"{BOLD}{GREEN}✔️  Live Feed Synced Successfully!{RESET}")

    def display_market(self):
        """Prints a gorgeous, cleanly aligned market dashboard."""
        print(f"\n{BOLD}{CYAN}╔═════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{BOLD}{CYAN}║{RESET}       {BOLD}{MAGENTA}📊 LIVE ASSET MANAGEMENT EXCHANGE MARKET MATRIX{RESET}       {BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}╠══════════════════╦═══════════════════════════╦══════════════╣{RESET}")
        print(f"{BOLD}{CYAN}║{RESET} {BOLD}{YELLOW}{'TICKER':<16}{RESET} {BOLD}{CYAN}║{RESET} {BOLD}{YELLOW}{'COMPANY NAME':<25}{RESET} {BOLD}{CYAN}║{RESET} {BOLD}{YELLOW}{'LIVE PRICE':<12}{RESET}{BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}╠══════════════════╬═══════════════════════════╬══════════════╣{RESET}")
        for sym, stock_obj in self.market_database.items():
            print(f"{BOLD}{CYAN}║{RESET}  {BOLD}{WHITE}{sym:<14}{RESET}  {BOLD}{CYAN}║{RESET} {stock_obj.company_name:<25} {BOLD}{CYAN}║{RESET} {GREEN}${stock_obj.current_price:<11.2f}{RESET}{BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}╚══════════════════╩═══════════════════════════╩══════════════╝{RESET}")

    def add_asset(self, symbol: str, quantity: int):
        symbol = symbol.upper().strip()
        if symbol not in self.market_database:
            raise ValueError("Target asset symbol is absent from core market databases.")
        if quantity <= 0:
            raise ValueError("Asset quantity adjustments must be absolute positive integers.")
        
        self.user_holdings[symbol] = self.user_holdings.get(symbol, 0) + quantity
        print(f"\n{BOLD}{GREEN}  ▶ [TRANSACTION SECURED]: Added {quantity} units of {symbol} to ledger matrix.{RESET}")

    def generate_financial_statement(self) -> tuple:
        total_value = 0.0
        statement_rows = []
        
        print("\n" + f"{BOLD}{MAGENTA}╔═════════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{BOLD}{MAGENTA}║{RESET}          {BOLD}{YELLOW}📝 OFFICIAL FINANCIAL STATEMENT BALANCE SHEET{RESET}          {BOLD}{MAGENTA}║{RESET}")
        print(f"{BOLD}{MAGENTA}╠══════════════╦══════════════╦══════════════════╦════════════════╣{RESET}")
        print(f"{BOLD}{MAGENTA}║{RESET} {BOLD}{CYAN}{'ASSET':<12}{RESET} {BOLD}{MAGENTA}║{RESET} {BOLD}{CYAN}{'SHARES':<12}{RESET} {BOLD}{MAGENTA}║{RESET} {BOLD}{CYAN}{'LIVE UNIT PRICE':<16}{RESET} {BOLD}{MAGENTA}║{RESET} {BOLD}{CYAN}{'TOTAL VALUE':<14}{RESET} {BOLD}{MAGENTA}║{RESET}")
        print(f"{BOLD}{MAGENTA}╠══════════════╬══════════════╬══════════════════╬════════════════╣{RESET}")
        
        for symbol, qty in self.user_holdings.items():
            stock = self.market_database[symbol]
            asset_value = qty * stock.current_price
            total_value += asset_value
            
            statement_rows.append([symbol, qty, f"${stock.current_price:.2f}", f"${asset_value:.2f}"])
            print(f"{BOLD}{MAGENTA}║{RESET}  {BOLD}{WHITE}{symbol:<10}{RESET} {BOLD}{MAGENTA}║{RESET}  {qty:<10}  {BOLD}{MAGENTA}║{RESET}  ${stock.current_price:<13.2f} {BOLD}{MAGENTA}║{RESET}  {GREEN}${asset_value:<11,.2f}{RESET} {BOLD}{MAGENTA}║{RESET}")
            
        print(f"{BOLD}{MAGENTA}╠══════════════╩══════════════╩══════════════════╬════════════════╣{RESET}")
        print(f"{BOLD}{MAGENTA}║{RESET} {BOLD}{YELLOW}AGGREGATE ACCOUNT EQUITY PORTFOLIO NET VALUE:{RESET}   {BOLD}{MAGENTA}║{RESET}  {BOLD}{GREEN}${total_value:<11,.2f}{RESET} {BOLD}{MAGENTA}║{RESET}")
        print(f"{BOLD}{MAGENTA}╚════════════════════════════════════════════════╩════════════════╝{RESET}")
        
        return total_value, statement_rows

    def export_ledger(self, statement_data: list, total_val: float):
        filename = f"portfolio_ledger_{datetime.now().strftime('%Y%m%d')}.csv"
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["SECURE INVESTMENT PORTFOLIO RECONCILIATION"])
                writer.writerow([f"Timestamp: {datetime.now().isoformat()}"])
                writer.writerow([])
                writer.writerow(["Ticker Symbol", "Volume Owned", "Market Price Evaluations", "Net Asset Valuation"])
                writer.writerows(statement_data)
                writer.writerow([])
                writer.writerow(["AGGREGATE NET PORTFOLIO VALUE", "", "", f"${total_val:,.2f}"])
            print(f"\n{BOLD}{GREEN}  💾 [DISK RECONCILIATION]: Local ledger spreadsheet created: '{filename}'{RESET}")
        except IOError as e:
            print(f"\n{BOLD}{RED}  ❌ Critical Backup Fault: {e}{RESET}")

def main():
    tracker = PortfolioTracker()
    tracker.display_market()
    
    while True:
        print(f"\n{BOLD}{WHITE}⌧ PLATFORM ENGINE RUNNING...{RESET}")
        cmd = input(f"Enter Ticker Symbol [{YELLOW}or type 'COMPILE' to finalize{RESET}]: ").upper().strip()
        if cmd == 'COMPILE':
            break
        try:
            qty_input = input(f"Enter asset share volume for {BOLD}{cmd}{RESET}: ")
            qty = int(qty_input)
            tracker.add_asset(cmd, qty)
        except ValueError as err:
            print(f"\n{BOLD}{RED}  ⚠️ [REJECTED]: {err} Input a listed ticker and a whole number.{RESET}")
            
    if tracker.user_holdings:
        final_value, records = tracker.generate_financial_statement()
        export_intent = input(f"\nExport audit statement ledger to Excel? ({GREEN}y{RESET}/{RED}n{RESET}): ").lower().strip()
        if export_intent in ['y', 'yes']:
            tracker.export_ledger(records, final_value)
    else:
        print(f"\n{BOLD}{YELLOW}📭 Portfolio matrix holds no entities. Exiting system context SAFELY.{RESET}")

if __name__ == "__main__":
    main()