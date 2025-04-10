import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, Subject} from 'rxjs';
import { tap } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private apiUrl = 'http://127.0.0.1:8000/products/api/products/';
  private apiUrlGender = 'http://127.0.0.1:8000/products/'
  private baseUrl = 'http://127.0.0.1:8000'; 

  
  constructor(private http: HttpClient) {}
  private productAddedSubject = new Subject<void>();

  getProducts(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  deleteProductFromBasket(user_id: number, product_id: number): Observable<any> {
    const url = `http://127.0.0.1:8000/basket/api/Basket/delete_from_basket/`; // Update the URL as per your Django configuration
    const options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
      body: { user_id, product_id },
    };
  
    return this.http.delete(url, options);
  }
  
  getProductsByGender(gender: string): Observable<any[]> {
    const url = `${this.apiUrlGender}${gender.toUpperCase()}`;
    return this.http.get<any[]>(url);
  }

  getTotalPrice(userId: number): Observable<number> {
    const url = `${this.baseUrl}/basket/${userId}/get_total_price/`;
    return this.http.get<number>(url);
  }

  getProductsInBasket(basket_id: number): Observable<any[]> {
    const url = `${this.baseUrl}/users/api/users/${basket_id}/get_products_in_basket/`;
    return this.http.get<any[]>(url);
  }

  getCurrentBasketId(userId: number): Observable<number> {
    const url = `${this.baseUrl}/users/api/users/${userId}/get_current_basket_id/`; 
    return this.http.get<number>(url);
  }
  
  addToBasket(userId: number, productId: number): Observable<any> {
    const url = `${this.baseUrl}/basket/api/Basket/add_to_basket/`; 
    const data = { user_id: userId, product_id: productId };
  
    return this.http.post<any>(url, data).pipe(
      tap(() => {
        // Trigger a refresh of the displayed products after a successful addition
        this.productAddedSubject.next(); 
      })
    );
  }

  // Function to subscribe to product added events
  onProductAdded(): Observable<void> {
      return this.productAddedSubject.asObservable();
    }

  updateProductStatus(productId: number): Observable<any> {
    const url = `${this.baseUrl}/products/update_product_status/${productId}/`;
    return this.http.post<any>(url, {});
  }

  checkout(userId: number): Observable<any> {
    const checkoutUrl = `${this.baseUrl}/basket/${userId}/checkout/`;
    return this.http.post(checkoutUrl, null);
  }

}