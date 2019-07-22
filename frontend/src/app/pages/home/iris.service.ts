import {Injectable} from '@angular/core';
import {Http} from "@angular/http";
import {Observable} from "rxjs/Observable";
import 'rxjs/add/operator/map';
import {
    Iris,
    Courses
   // ProbabilityPrediction,
    //SVCParameters,
    //SVCResult
} from "./types";
import { jsonpFactory } from '@angular/http/src/http_module';

const SERVER_URL: string = 'api/';

@Injectable()
export class IrisService {
    constructor(private http: Http) {
    }

    grad_courses:string[] = []
    
    public predictIris(iris: Iris):Observable<Courses[]> {
        return this.http.post(`${SERVER_URL}predict`, iris).map((res) => res.json());
    }
}
